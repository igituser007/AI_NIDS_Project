1. Project Overview & Process (Executive Summary)
The goal of this project was to develop a proactive security layer capable of identifying network threats using artificial intelligence. Unlike traditional firewalls that rely on a "list of known bad actors," this system analyzes traffic behavior.

The Development Process:

Requirement Gathering: Identified key network features (Port, Duration, Packet Size) that signal an attack.

Environment Setup: Configured a Python-based workspace using Jupyter for development and Streamlit for deployment.

Data Engineering: Created a synthetic dataset based on the CIC-IDS2017 structure to train the model on diverse traffic patterns.

Model Selection: Implemented Random Forest due to its ability to handle high-dimensional data and prevent "overfitting."

UI Integration: Developed a web-based dashboard for real-time interaction and forensic analysis.

2. Technical Requirements
To replicate this project, the following dependencies are required:

Software:

Python 3.8+

Jupyter Lab / Notebook (For development)

Web Browser (To view the dashboard)

Python Libraries:
pandas          # Data manipulation
numpy           # Numerical calculations
scikit-learn    # Machine Learning algorithms
streamlit       # Web UI framework
seaborn         # Statistical data visualization
matplotlib      # Plotting engine

3. Result Analysis
After training the model on 5,000 simulated network sessions, the following results were observed:

Accuracy: The model consistently achieved 95% - 98% accuracy on the test set.

Detection Rate: The system showed a high success rate in identifying "Flood" type attacks (characterized by high packet counts and duration).

Precision vs. Recall: * Precision: High precision ensures that "Safe" traffic is rarely flagged as an alert (minimizing false alarms).

Recall: High recall ensures that actual "Attacks" are caught and not missed.

4. Final Conclusion
The implementation of the Sentinel AI NIDS demonstrates that Random Forest Classifiers are highly effective for network security. By shifting from signature-based detection to behavior-based detection, we have created a system that can adapt to new, unseen threats.

Key Achievements:

Successfully bridged the gap between a complex ML model and a user-friendly UI.

Reduced the technical barrier for security analysts to perform "what-if" forensic testing via the Live Simulator.

Proved that open-source tools (Python/Streamlit) are sufficient for building high-performance security prototypes.

Future Scope: The next version of this project could integrate Scapy for live packet sniffing on a local area network (LAN) and implement Deep Learning (LSTM) to analyze time-series patterns in traffic more effectively.



