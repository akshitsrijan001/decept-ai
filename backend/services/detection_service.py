from ast import keyword
from email.mime import text
from difflib import SequenceMatcher
DARK_PATTERNS = {

    "scarcity": [
        "only",
        "few remaining",
        "limited stock",
        "almost gone",
        "selling fast",
        "last chance",
        "hurry before sold out"
    ],

    "urgency": [
        "limited offer",
        "offer ends",
        "expires",
        "expires today",
        "expires soon",
        "today only",
        "ending soon",
        "hurry"
    ],

    "pressure": [
        "buy now",
        "act now",
        "claim now",
        "don't miss",
        "instant access",
        "get it now"
    ],

    "confirmshaming": [
    "no thanks",
    "thanks",
    "i don't want to save",
    "i don't like discounts",
    "i'll pay full price",
    "pay full price",
    "continue without savings"
    ],

    "social_proof": [
    "people bought",
    "customers purchased",
    "viewing this now",
    "popular choice",
    "best seller",
    "trending now",
    "most popular",
    "top rated",
    "high demand",
    "customer favorite",
    "frequently bought",
    "recommended by users",
    "join thousands",
    "trusted by",
    "millions of users",
    "used by thousands",
    "most popular",
    "trusted by thousands",
    "join thousands of users",
    "used by millions",
    "customer favorite",
    "most viewed",
    "top choice",
    "recommended product",
    "customers love",
    "people are buying",
    "popular right now",
    "highly rated",
    "five star choice",
    "market leader",
    "top pick",
    ],

    "subscription_trap": [
    "free trial",
    "cancel anytime",
    "start free trial",
    "auto renew",
    "subscription required",
    "continue membership"
    ],

}

    


PATTERN_EXPLANATIONS = {

    "scarcity":
        "Creates fear of missing out by implying limited availability.",

    "urgency":
        "Encourages immediate action through time pressure.",

    "pressure":
        "Pushes users toward a decision using persuasive commands.",

    "confirmshaming":
        "Uses guilt or negative wording to discourage opting out.",

    "social_proof":
        "Influences decisions using popularity or crowd behaviour.",

    "subscription_trap":
        "Encourages signups that may lead to recurring charges."

}
OCR_CORRECTIONS = {
    "noh": "now",
    "nov": "now",
    "nowl": "now",
    "lirnited": "limited",
    "limitedd": "limited",
    "offcr": "offer",
    "offef": "offer",
    "ofter": "offer",
    "tirne": "time",
    "anytirne": "anytime",
    "rnembership": "membership",
    "buv": "buy",
    "clairn": "claim",
    "hurrv": "hurry",
    "todav": "today",
    "triai": "trial",
    "cancei": "cancel",
    "peopie": "people",
    "custorners": "customers",
    "thousancls": "thousands",
    "popuiar": "popular",
    "seiler": "seller",
}
KNOWN_PHRASES = [
    "only",
    "limited",
    "offer",
    "act",
    "now",
    "buy",
    "claim",
    "free",
    "trial",
    "membership",
    "subscription",
    "cancel",
    "anytime",
    "seller",
    "popular",
    "people",
    "customers",
    "hurry",
    "today",
    "expires",
]
def fuzzy_correct_word(word):

    best_match = word
    highest_score = 0

    for phrase in KNOWN_PHRASES:

        similarity = SequenceMatcher(
            None,
            word,
            phrase
        ).ratio()

        if similarity > highest_score:
            highest_score = similarity
            best_match = phrase

    if highest_score >= 0.75:
        return best_match

    return word


def correct_ocr_text(text):

    corrected = text

    for wrong, right in OCR_CORRECTIONS.items():
        corrected = corrected.replace(
            wrong,
            right
        )

    words = corrected.split()

    words = [
        fuzzy_correct_word(word)
        for word in words
    ]
    print("CORRECTED OCR:", " ".join(words))
    return " ".join(words)

def analyze_text(text):

    text = text.lower()
    print("OCR TEXT:", text)

    text = correct_ocr_text(text)
    print("FINAL OCR TEXT:")
    print(repr(text))
    print("CORRECTED OCR:", text)

    detected = []
    score = 0
    matches = {}

    PHRASE_WEIGHTS = {

        # Scarcity
        "only": 10,
        "few remaining": 20,
        "limited stock": 20,
        "almost gone": 20,
        "selling fast": 15,
        "last chance": 20,
        "hurry before sold out": 25,

        # Urgency
        "limited offer": 20,
        "offer ends": 20,
        "expires": 15,
        "expires today": 25,
        "expires soon": 20,
        "today only": 20,
        "ending soon": 20,
        "hurry": 15,

        # Pressure
        "buy now": 15,
        "act now": 15,
        "claim now": 15,
        "don't miss": 20,
        "instant access": 10,
        "get it now": 15,

        # Social Proof
        "best seller": 15,
        "trending now": 15,
        "people bought": 15,
        "most popular": 15,
        "top rated": 15,
        "high demand": 15,
        "customer favorite": 15,
        "frequently bought": 15,
        "recommended by users": 15,
        "join thousands": 20,
        "trusted by": 20,
        "millions of users": 20,
        "used by thousands": 20,

        # Subscription Trap
        "free trial": 20,
        "start free trial": 25,
        "cancel anytime": 20,
        "continue membership": 25,

        # Confirmshaming
        "no thanks": 10,
        "thanks": 5,
        "i'll pay full price": 20,
        "pay full price": 15,
        "continue without savings": 20,
        "no i prefer paying more": 20,
        "i hate saving money": 20,
        "skip savings": 15,
        "continue without discount": 20,
        "continue without offer": 20,
        "i don't want discounts": 20,
        "leave savings behind": 20,
    }

    for category, keywords in DARK_PATTERNS.items():

        for keyword in keywords:
            print("CHECK:", keyword)
            print("COUNT:", text.count(keyword))

            count = text.count(keyword)

            if count > 0:

                detected.append(category)

                score += (
                    PHRASE_WEIGHTS.get(keyword, 10)
                    * count
                )

                if category not in matches:
                    matches[category] = []

                matches[category].append(keyword)

    detected = list(set(detected))

    if len(detected) >= 3:
        score += 15

    elif len(detected) == 2:
        score += 10

    score = min(score, 100)

    if score < 40:
        risk = "Low"
    elif score < 70:
        risk = "Medium"
    else:
        risk = "High"

    pattern_count = len(detected)

    confidence = min(
    40 + (pattern_count * 15) + (score // 4),
    100
)

    print("PATTERNS:", detected)
    print("MATCHES:", matches)
    print("SCORE:", score)

    return {
        "score": score,
        "risk": risk,
        "patterns": detected,
        "matches": matches,
        "explanations": {
            pattern: PATTERN_EXPLANATIONS[pattern]
            for pattern in detected
        },
        "confidence": confidence
    }
