import React, { useState } from 'react';
import axios from 'axios';

const PredictOutcome = () => {
  const [bowlingType, setBowlingType] = useState('');
  const [shotType, setShotType] = useState('');
  const [shotTiming, setShotTiming] = useState('');
  const [outcome, setOutcome] = useState('');
  const [commentary, setCommentary] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', {
        bowling_type: bowlingType,
        shot_type: shotType,
        shot_timing: shotTiming
      });
      setOutcome(response.data.outcome);
      setCommentary(response.data.commentary);
    } catch (error) {
      console.error("Error fetching prediction", error);
    }
  };

  return (
    <div className="predict-outcome">
      <h2>Predict Shot Outcome</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Bowling Type:
          <input type="text" value={bowlingType} onChange={(e) => setBowlingType(e.target.value)} required />
        </label>
        <label>
          Shot Type:
          <input type="text" value={shotType} onChange={(e) => setShotType(e.target.value)} required />
        </label>
        <label>
          Shot Timing:
          <select value={shotTiming} onChange={(e) => setShotTiming(e.target.value)} required>
            <option value="">Select Timing</option>
            <option value="Early">Early</option>
            <option value="Good">Good</option>
            <option value="Perfect">Perfect</option>
            <option value="Late">Late</option>
          </select>
        </label>
        <button type="submit">Predict Outcome</button>
      </form>
      {outcome && (
        <div className="result">
          <h3>Outcome: {outcome}</h3>
          <p>Commentary: {commentary}</p>
        </div>
      )}
    </div>
  );
};

export default PredictOutcome;
