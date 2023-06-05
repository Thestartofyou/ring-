from ring_doorbell import Ring, Auth

# Authenticate with your Ring account
ring_email = "YOUR_RING_EMAIL"
ring_password = "YOUR_RING_PASSWORD"
auth = Auth("my_token.json")
auth.fetch_token(ring_email, ring_password)

# Connect to your Ring Doorbell
ring = Ring(auth)

def count_people_detected():
    # Get the list of events from your Ring Doorbell
    events = ring.doorbell("YOUR_DOORBELL_ID").history(limit=50)  # Adjust the limit as needed

    count = 0
    for event in events:
        # Check if the event is a motion event and it detected people
        if event['kind'] == 'motion' and event['kind'] == 'person':
            count += 1

    return count

# Example usage
people_count = count_people_detected()
print(f"Number of people detected: {people_count}")
