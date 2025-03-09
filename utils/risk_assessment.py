# utils/risk_assessment.py
# This module contains the function to classify risk levels based on probability scores.

def get_risk_level(probability):
    """
    Determines the risk level based on the probability of having a disease.

    Args:
    - probability (float): Probability score (between 0 and 1).

    Returns:
    - str: Risk level (Low, Moderate, or High).
    """
    if probability <= 0.4:
        return "Low Risk"
    elif probability <= 0.7:
        return "Moderate Risk"
    else:
        return "High Risk"
