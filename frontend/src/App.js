import React from 'react';
import PredictOutcome from './components/PredictOutcome';
import SuperOverSimulator from './components/SuperOverSimulator';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Cricket Predictor</h1>
      <div className="container">
        <PredictOutcome />
        <SuperOverSimulator />
      </div>
    </div>
  );
}

export default App;
