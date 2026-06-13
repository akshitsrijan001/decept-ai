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
    "trending now"
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
    "lirnited": "limited",
    "offcr": "offer",
    "tirne": "time",
    "anytirne": "anytime",
    "rnembership": "membership",

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

    "cancel",
    "anytime",

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
    }

    for category, keywords in DARK_PATTERNS.items():

        for keyword in keywords:

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

    confidence = min(score, 100)

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
