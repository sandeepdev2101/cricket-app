# coding=utf-8
import random
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# Step 1: Outcome Chart for Shot Outcome Prediction
outcome_chart = {
    "Bouncer": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Flick": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Wicket"},
        "Long On": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "LegLance": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Wicket"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
    },
    "Outswinger": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Yorker": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "SquareCut": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Bowled"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "UpperCut": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Bowled"},
    },
    "Off Break": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
    },
    "Inswinger": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Leg Cutter": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Slower Ball": {
        "Straight": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "LBW"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Pace": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Off Cutter": {
        "Straight": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "2 runs", "Perfect": "4 runs", "Late": "Caught"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Doosra": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "LBW"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    },
    "Reverse Swing": {
        "Straight": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Flick": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
        "Long On": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "SquareCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "Sweep": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Bowled"},
        "CoverDrive": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Pull": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "Scoop": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught"},
        "LegLance": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Wicket"},
        "UpperCut": {"Early": "1 run", "Good": "4 runs", "Perfect": "6 runs", "Late": "Caught Behind"},
    }
}


# Step 2: Commentary based on outcome
commentary_map = {
    "Wicket": "Edged and taken - 0 runs",
    "6 runs": "Thats massive and out of the ground.",
    "4 runs": "Just over the fielder.",
    "2 runs": "Excellent running between the wickets.",
    "1 run": "Convert ones into twos.",
    "Bowled": "Its a wicket. Excellent line and length.",
}

def predict_outcome(bowling_type, shot_type, shot_timing):
    """ Predict shot outcome based on bowling type, shot type, and shot timing """
    try:
        outcome = outcome_chart[bowling_type][shot_type][shot_timing]
        return outcome
    except KeyError:
        return None  # Return None for invalid combinations

def get_commentary(outcome):
    """ Get suitable commentary based on the outcome """
    return commentary_map.get(outcome, "Great effort.")

# Step 3: Super Over Simulation
def simulate_super_over(bowling_types, shots):
    """ Simulate a super over and provide commentary for each ball """
    wickets = 2
    runs = 0
    commentary = []
    for i in range(6):
        if wickets == 0:
            break
        ball = bowling_types[i]
        shot = shots[i]
        shot_name, shot_timing = shot

        # Predict outcome
        outcome = predict_outcome(ball, shot_name, shot_timing)
        
        if not outcome:
            commentary.append(f"Ball {i+1}: Invalid combination for {ball}, {shot_name}, {shot_timing}")
            continue

        if outcome in ("Wicket", "Bowled", "LBW", "Caught", "Caught Behind"):
            wickets -= 1
        else:
            runs += int(outcome.split()[0])

        # Get commentary
        comment = get_commentary(outcome)
        
        commentary.append(f"Ball {i+1}: {ball} bowled, Shot {shot_name} played {shot_timing} - {comment} - {outcome}")
    
    return runs, wickets, commentary

@app.route('/predict', methods=['POST'])
def predict():
    """ Handle shot outcome prediction """
    data = request.json
    required_keys = ['bowling_type', 'shot_type', 'shot_timing']
    
    # Check if all required keys are present
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Invalid input. Required fields: bowling_type, shot_type, shot_timing."}), 400
    
    bowling_type = data['bowling_type']
    shot_type = data['shot_type']
    shot_timing = data['shot_timing']
    
    # Predict the outcome
    outcome = predict_outcome(bowling_type, shot_type, shot_timing)
    
    if not outcome:
        return jsonify({
            "outcome": f"Invalid combination for {bowling_type}, {shot_type}, {shot_timing}.",
            'commentary': None
        })

    # Get commentary
    commentary = get_commentary(outcome)
    
    return jsonify({
        'outcome': outcome,
        'commentary': commentary
    })

@app.route('/superover', methods=['POST'])
def superover():
    """ Simulate a Super Over and return the commentary and result """
    data = request.json
    if 'shots' not in data:
        return jsonify({"error": "Invalid input. Shots field is required."}), 400
    
    shots = data['shots']  # List of tuples [(shot_name1, shot_timing1), (shot_name2, shot_timing2), ...]
    
    if not isinstance(shots, list) or len(shots) != 6:
        return jsonify({"error": "Invalid input. Exactly 6 shots are required."}), 400

    for shot in shots:
        if not isinstance(shot, list) or len(shot) != 2:
            return jsonify({"error": f"Invalid shot input: {shot}. Each shot must be a tuple of (shot_name, shot_timing)."}), 400
    
    target = 21  # Fixed target for this challenge
    bowling_types = ["Bouncer", "Inswinger", "Outswinger", "Leg Cutter", "Off Cutter", "Reverse Swing"]  # Example bowling types
    
    # Simulate super over
    runs, wickets, commentary = simulate_super_over(bowling_types, shots)
    
    # Determine result
    if runs >= target:
        result = f"AUSTRALIA won by {2 - wickets} wickets"
    else:
        result = f"AUSTRALIA lost by {target - runs} runs"
    
    return jsonify({
        'runs': runs,
        'wickets': 2 - wickets,
        'commentary': commentary,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
