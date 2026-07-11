import numpy as np

def calculate_space_mean_speed(travel_distances, travel_times):
    """
    Calculates Space Mean Speed (SMS), a critical variable in traffic flow theory.
    Formula: SMS = Total Distance / Total Time taken by all vehicles.
    """
    total_distance = sum(travel_distances)
    total_time = sum(travel_times)
    
    if total_time == 0:
        return 0
    return total_distance / total_time

def evaluate_linear_speed_density(density, free_flow_speed, jam_density):
    """
    Applies Greenshields' linear speed-density model to estimate 
    the equilibrium speed of the traffic stream.
    """
    if density >= jam_density:
        return 0.0
    # Linear relationship calculation
    estimated_speed = free_flow_speed * (1.0 - (density / jam_density))
    return round(estimated_speed, 2)

if __name__ == "__main__":
    print("--- Traffic Analytics & Road Safety System ---")
    
    # Mock data for a section of a road (Distance in km, Time in hours)
    distances = [1.5, 1.5, 1.5, 1.5] 
    times = [0.026, 0.025, 0.027, 0.026] # approx 57 km/h average
    
    sms = calculate_space_mean_speed(distances, times)
    print(f"Calculated Space Mean Speed: {sms:.2f} km/h")
    
    # Scenario: High-density peak hours
    current_density = 45  # vehicles/km
    free_speed = 80       # km/h
    jam_density = 120     # vehicles/km
    
    predicted_speed = evaluate_linear_speed_density(current_density, free_speed, jam_density)
    print(f"Predicted Stream Speed under current density ({current_density} veh/km): {predicted_speed} km/h")
