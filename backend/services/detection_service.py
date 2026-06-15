from ast import keyword
from email.mime import text
from difflib import SequenceMatcher
DARK_PATTERNS = {

    "scarcity": {
        "only": 10,
        "only 1 left": 20,
        "only 2 left": 18,
        "only 3 left": 16,
        "few left": 15,
        "running out": 15,
        "low stock": 15,
        "almost sold out": 20,
        "selling quickly": 15,
        "selling out fast": 18,
        "limited quantity": 18,
    },

    "urgency": {
        "limited offer": 15,
        "offer expires": 15,
        "expires": 12,
        "expires today": 20,
        "expires soon": 15,
        "today only": 15,
        "ending soon": 15,
        "hurry": 10,
        "sale ends tonight": 20,
        "countdown": 18,
        "last day": 18,
        "offer ending": 15,
        "time running out": 20,
    },

    "pressure": {
        "buy now": 15,
        "act now": 15,
        "claim now": 15,
        "don't miss": 15,
        "instant access": 10,
        "get it now": 15,
        "shop now": 15,
        "don't wait": 15,
        "start now": 12,
        "join now": 12,
        "unlock now": 12,
        "get started": 10,
    },

    "confirmshaming": {
        "no thanks": 10,
        "thanks": 5,
        "i don't want to save": 20,
        "i don't like discounts": 20,
        "i'll pay full price": 20,
        "pay full price": 15,
        "continue without savings": 20,
        "continue without discount": 20,
        "continue without offer": 20,
        "skip savings": 15,
    },

    "social_proof": {
    "people bought": 15,
    "customers purchased": 15,
    "viewing this now": 15,
    "popular choice": 15,
    "best seller": 18,
    "trending now": 15,
    "most popular": 18,
    "top rated": 15,
    "high demand": 15,
    "customer favorite": 15,
    "frequently bought": 15,
    "recommended by users": 15,
    "join thousands": 20,
    "trusted by": 20,
    "millions of users": 20,
    "used by thousands": 20,
    "trusted by thousands": 25,
    "join thousands of users": 25,
    "used by millions": 25,
    "customers love": 15,
    "market leader": 15,
    },

    "subscription_trap": {
    "free trial": 15,
    "start free trial": 20,
    "cancel anytime": 15,
    "auto renew": 20,
    "subscription required": 20,
    "continue membership": 20,
    "automatically renewed": 20,
    },

    "fomo": {
    "don't miss out": 20,
    "everyone is buying": 20,
    "be part of": 10,
    "last opportunity": 20,
    "exclusive access": 15,
    "missing out": 15,
    "join thousands today": 20,
    "limited seats": 20,
    "popular right now": 15,
    },

    "authority_bias": {
    "expert recommended": 15,
    "doctor approved": 20,
    "recommended by experts": 15,
    "used by professionals": 15,
    "industry leader": 15,
    "trusted experts": 15,
    "official recommendation": 15,
    "professional choice": 15,
    "scientifically proven": 20,
    "certified solution": 15,
    },

    "emotional_manipulation": {
    "you will regret it": 25,
    "don't be left out": 20,
    "why wait": 10,
    "your family deserves": 20,
    "protect your loved ones": 25,
    "act before it's too late": 25,
    "avoid disappointment": 20,
    "don't miss this chance": 20,
    "make the smart choice": 10,
    },

    "default_opt_in": {
    "preselected":20,
    "automatically selected":25,
    "default option":15,
    "automatically renewed":30,
    "included by default":20,
    "opt out":15,
    "automatic enrollment":30,
    "auto selected":20
    },

    "hidden_costs": {
    "additional fees apply": 25,
    "service charge": 20,
    "processing fee": 20,
    "handling fee": 20,
    "convenience fee": 20,
    "extra charges": 20,
    "taxes not included": 25,
    "fees may apply": 20,
    "charges apply": 20,
    }
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
        "Encourages signups that may lead to recurring charges.",

    "fomo":
        "Creates fear of missing out to influence user decisions.",

    "authority_bias":
        "Uses authority figures or expertise to influence choices.",

    "emotional_manipulation":
        "Uses emotional triggers to pressure decisions.",

    "default_opt_in":
        "Preselects choices that may benefit the provider.",

    "hidden_costs":
        "Conceals or delays disclosure of extra charges.",

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

    CATEGORY_WEIGHTS = {
        "scarcity": 15,
        "urgency": 15,
        "pressure": 10,
        "social_proof": 10,
        "confirmshaming": 20,
        "subscription_trap": 20,
        "fomo": 15,
        "authority_bias": 10,
        "emotional_manipulation": 15,
        "default_opt_in": 20,
        "hidden_costs": 20,
}

    PHRASE_WEIGHTS = {

        # Scarcity
        "only": 10,
        "few remaining": 20,
        "limited stock": 20,
        "almost gone": 20,
        "selling fast": 15,
        "last chance": 20,
        "hurry before sold out": 25,
        "only": 10,
        "only 1 left": 20,
        "only 2 left": 18,
        "only 3 left": 16,
        "few left": 15,
        "running out": 15,
        "low stock": 15,
        "almost sold out": 20,
        "selling quickly": 15,
        "selling out fast": 18,
        "limited quantity": 18,

        # Urgency
        "limited offer": 20,
        "offer ends": 20,
        "expires": 15,
        "expires today": 25,
        "expires soon": 20,
        "today only": 20,
        "ending soon": 20,
        "hurry": 15,
        "limited offer": 15,
        "offer expires": 15,
        "expires": 12,
        "expires today": 20,
        "expires soon": 15,
        "today only": 15,
        "ending soon": 15,
        "hurry": 10,
        "sale ends tonight": 20,
        "countdown": 18,
        "last day": 18,
        "offer ending": 15,
        "time running out": 20,

        # Pressure
        "buy now": 15,
        "act now": 15,
        "claim now": 15,
        "don't miss": 20,
        "instant access": 10,
        "get it now": 15,
        "buy now": 15,
        "act now": 15,
        "claim now": 15,
        "don't miss": 15,
        "instant access": 10,
        "get it now": 15,
        "shop now": 15,
        "don't wait": 15,
        "start now": 12,
        "join now": 12,
        "unlock now": 12,
        "get started": 10,

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
        "people bought": 15,
        "customers purchased": 15,
        "viewing this now": 15,
        "popular choice": 15,
        "trusted by thousands": 25,
        "used by millions": 25,
        "customers love": 15,
        "market leader": 15,
        
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
                    + CATEGORY_WEIGHTS.get(category, 10)
                    * count
                )

                if category not in matches:
                    matches[category] = []

                matches[category].append(keyword)

    detected = list(set(detected))
    # Synergy bonuses

    if "scarcity" in detected and "urgency" in detected:
        score += 5

    if (
        "scarcity" in detected
        and "urgency" in detected
        and "pressure" in detected
    ):
        score += 8

    if (
        "subscription_trap" in detected
        and "confirmshaming" in detected
    ):
        score += 20

    if (
        "social_proof" in detected
        and "fomo" in detected
    ):
        score += 15

        if len(detected) >= 3:
            score += 8

        elif len(detected) == 2:
            score += 5

    score = min(score, 100)

    if score < 40:
        risk = "Low"
    elif score < 75:
        risk = "Medium"
    else:
        risk = "High"

    pattern_count = len(detected)

    confidence = min(
    50
    + (pattern_count * 10)
    + (score // 5),
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
