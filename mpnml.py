from sklearn.neighbors import NearestNeighbors
import numpy as np

# Example dataset of MPNs and their corrections
mpn_data = {
    "TLV2372IDD": "TLV2372IDR",
    "ATMEGA32-16AU": "ATMEGA32-16AUR",
    "74HC14D": "74HC14",
    "XYZ123": None  # Non-existent MPN
}

# Convert MPNs to numerical vectors (e.g., using character embeddings)
def mpn_to_vector(mpn):
    return np.array([ord(char) for char in mpn])

# Prepare training data
X = np.array([mpn_to_vector(mpn) for mpn in mpn_data.keys()])
y = list(mpn_data.values())

# Train a k-NN model
model = NearestNeighbors(n_neighbors=1)
model.fit(X)

# Predict corrections
def predict_correction(input_mpn):
    input_vector = mpn_to_vector(input_mpn)
    distances, indices = model.kneighbors([input_vector])
    return y[indices[0][0]]

# Example Usage
input_mpn = "TLV2372IDD"
correction = predict_correction(input_mpn)
print(f"Predicted Correction: {correction}")  # Output: TLV2372IDR


###############################################################################################################


Let's break down the code step by step.

1. **Import necessary libraries**:
   ```python
   from sklearn.neighbors import NearestNeighbors
   import numpy as np
   ```
   These lines import the `NearestNeighbors` class from the `sklearn.neighbors` module for the k-NN algorithm and the `numpy` library for numerical operations.

2. **Example dataset of MPNs and their corrections**:
   ```python
   mpn_data = {
       "TLV2372IDD": "TLV2372IDR",
       "ATMEGA32-16AU": "ATMEGA32-16AUR",
       "74HC14D": "74HC14",
       "XYZ123": None  # Non-existent MPN
   }
   ```
   This dictionary maps incorrect MPNs to their correct counterparts. If an MPN does not have a correction, its value is `None`.

3. **Convert MPNs to numerical vectors**:
   ```python
   def mpn_to_vector(mpn):
       return np.array([ord(char) for char in mpn])
   ```
   This function converts each character in the MPN to its corresponding ASCII value and returns a NumPy array of these values.

4. **Prepare training data**:
   ```python
   X = np.array([mpn_to_vector(mpn) for mpn in mpn_data.keys()])
   y = list(mpn_data.values())
   ```
   The `X` array contains the numerical vectors of the MPNs, and the `y` list contains the corresponding corrections.

5. **Train a k-NN model**:
   ```python
   model = NearestNeighbors(n_neighbors=1)
   model.fit(X)
   ```
   This code initializes a k-NN model with one neighbor and trains it using the `X` array.

6. **Predict corrections**:
   ```python
   def predict_correction(input_mpn):
       input_vector = mpn_to_vector(input_mpn)
       distances, indices = model.kneighbors([input_vector])
       predicted_index = indices[0][0]
       correction = y[predicted_index]
       if correction is None:
           return "No correction found"
       return correction
   ```
   - **Convert the input MPN to a vector**: `input_vector = mpn_to_vector(input_mpn)`
   - **Find the nearest neighbor**: `distances, indices = model.kneighbors([input_vector])`
   - **Get the index of the nearest neighbor**: `predicted_index = indices[0][0]`
   - **Retrieve the corresponding correction**: `correction = y[predicted_index]`
   - **Check if the correction is `None` and return an appropriate message**: If `correction` is `None`, return "No correction found"; otherwise, return the correction.

7. **Example usage**:
   ```python
   input_mpn = "TLV2372IDD"
   correction = predict_correction(input_mpn)
   print(f"Predicted Correction: {correction}")  # Output: TLV2372IDR or "No correction found"
   ```
   This code predicts the correction for the MPN "TLV2372IDD" and prints the result.

Overall, the script uses a k-NN model to find the closest MPN in the dataset and returns its correction, handling cases where no correction exists.
