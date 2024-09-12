import React, { useState } from 'react';
import axios from 'axios';

const SuperOverSimulator = () => {
	const [shotData, setShotData] = useState({
		shot1: { name: "", timing: "" },
		shot2: { name: "", timing: "" },
		shot3: { name: "", timing: "" },
		shot4: { name: "", timing: "" },
		shot5: { name: "", timing: "" },
		shot6: { name: "", timing: "" }
	});
	const [result, setResult] = useState('');
	const [commentary, setCommentary] = useState([]);

	const handleChange = (e, shotNumber) => {
		const { name, value } = e.target;
		setShotData(prevState => ({
			...prevState,
			[shotNumber]: {
				...prevState[shotNumber],
				[name]: value
			}
		}));
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		const shots = [
			[`${shotData.shot1.name}`, `${shotData.shot1.timing}`],
			[`${shotData.shot2.name}`, `${shotData.shot2.timing}`],
			[`${shotData.shot3.name}`, `${shotData.shot3.timing}`],
			[`${shotData.shot4.name}`, `${shotData.shot4.timing}`],
			[`${shotData.shot5.name}`, `${shotData.shot5.timing}`],
			[`${shotData.shot6.name}`, `${shotData.shot6.timing}`]
		];
		try {
			const response = await axios.post('http://127.0.0.1:5000/superover', { shots });
			setResult(response.data.result);
			setCommentary(response.data.commentary);
		} catch (error) {
			console.error("Error fetching super over result", error);
		}
	};

	return (
		<div>
			<h2>Super Over Simulator</h2>
			<form onSubmit={handleSubmit}>
				{/* Shot 1 */}
				<div>
					<label>Shot 1 Name:</label>
					<input
						name="name"
						value={shotData.shot1.name}
						onChange={(e) => handleChange(e, "shot1")}
						required
					/>
					<label>Shot 1 Timing:</label>
					<select name="timing" value={shotData.shot1.timing} onChange={(e) => handleChange(e, "shot1")} required>
						<option value="">Select Timing</option>
						<option value="Early">Early</option>
						<option value="Good">Good</option>
						<option value="Perfect">Perfect</option>
						<option value="Late">Late</option>
					</select>
				</div>

				{/* Shot 2 */}
				<div>
					<label>Shot 2 Name:</label>
					<input
						name="name"
						value={shotData.shot2.name}
						onChange={(e) => handleChange(e, "shot2")}
						required
					/>
					<label>Shot 2 Timing:</label>
					<select name="timing" value={shotData.shot2.timing} onChange={(e) => handleChange(e, "shot2")} required>
						<option value="">Select Timing</option>
						<option value="Early">Early</option>
						<option value="Good">Good</option>
						<option value="Perfect">Perfect</option>
						<option value="Late">Late</option>
					</select>
				</div>

				{/* Shot 3 */}
				<div>
					<label>Shot 3 Name:</label>
					<input
						name="name"
						value={shotData.shot3.name}
						onChange={(e) => handleChange(e, "shot3")}
						required
					/>
					<label>Shot 3 Timing:</label>
					<select name="timing" value={shotData.shot3.timing} onChange={(e) => handleChange(e, "shot3")} required>
						<option value="">Select Timing</option>
						<option value="Early">Early</option>
						<option value="Good">Good</option>
						<option value="Perfect">Perfect</option>
						<option value="Late">Late</option>
					</select>
				</div>

				{/* Shot 4 */}
				<div>
					<label>Shot 4 Name:</label>
					<input
						name="name"
						value={shotData.shot4.name}
						onChange={(e) => handleChange(e, "shot4")}
						required
					/>
					<label>Shot 4 Timing:</label>
					<select name="timing" value={shotData.shot4.timing} onChange={(e) => handleChange(e, "shot4")} required>
						<option value="">Select Timing</option>
						<option value="Early">Early</option>
						<option value="Good">Good</option>
						<option value="Perfect">Perfect</option>
						<option value="Late">Late</option>
					</select>
				</div>

				{/* Shot 5 */}
				<div>
					<label>Shot 5 Name:</label>
					<input
						name="name"
						value={shotData.shot5.name}
						onChange={(e) => handleChange(e, "shot5")}
						required
					/>
					<label>Shot 5 Timing:</label>
					<select name="timing" value={shotData.shot5.timing} onChange={(e) => handleChange(e, "shot5")} required>
						<option value="">Select Timing</option>
						<option value="Early">Early</option>
						<option value="Good">Good</option>
						<option value="Perfect">Perfect</option>
						<option value="Late">Late</option>
					</select>
				</div>

				{/* Shot 6 */}
				<div>
					<label>Shot 6 Name:</label>
					<input
						name="name"
						value={shotData.shot6.name}
						onChange={(e) => handleChange(e, "shot6")}
						required
					/>
					<label>Shot 6 Timing:</label>
					<select name="timing" value={shotData.shot6.timing} onChange={(e) => handleChange(e, "shot6")} required>
						<option value="">Select Timing</option>
						<option value="Early">Early</option>
						<option value="Good">Good</option>
						<option value="Perfect">Perfect</option>
						<option value="Late">Late</option>
					</select>
				</div>

				<button type="submit">Submit</button>
			</form>

			{/* Display the result */}
			{result && (
				<div className='result'>
					<h3>Result: {result}</h3>
					<ul>
						{commentary.map((line, index)=>(
							<li key={index}>{line}</li>
						))}
					</ul>
				</div>
			)}
		</div>
	);
};

export default SuperOverSimulator;
