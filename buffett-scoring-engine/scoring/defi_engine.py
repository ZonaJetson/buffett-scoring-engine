def score_defi(protocol):
    data = {
        "LINK": {"revenue": 180_000_000, "treasury": 350_000_000, "burn": 0.02},
        "AAVE": {"revenue": 110_000_000, "treasury": 150_000_000, "burn": 0.01},
        "UNI":  {"revenue": 80_000_000, "treasury": 200_000_000, "burn": 0.00}
    }
    d = data.get(protocol, {})
    score = 0
    if d["revenue"] > 150_000_000:
        score += 20
    elif d["revenue"] > 100_000_000:
        score += 15
    else:
        score += 10
    if d["burn"] >= 0.02:
        score += 15
    elif d["burn"] > 0:
        score += 10
    else:
        score += 5
    return {"protocol": protocol, "score": score}
