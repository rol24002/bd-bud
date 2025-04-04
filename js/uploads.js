// Java Script for the Uploads Page

//java to do the appearing and disappearing of the upload and search area
//Event Listner
document.addEventListener('DOMContentLoaded', function() {
    const imageSearchButton = document.querySelector('.button-group button:nth-child(1)');
    const imageUploadButton = document.querySelector('.button-group button:nth-child(2)');
    const uploadArea = document.querySelector('.upload-area');
    const searchArea = document.querySelector('.search-area');
    const resultsDiv = document.getElementById('identificationResults');
    const imageUploadInput = document.getElementById('uploadedImage');
    const submitButton = document.getElementById('submitButton');

    // Initially hide both areas
    uploadArea.style.display = 'none';
    searchArea.style.display = 'none';
  
    // Show the search area when cliocked
    imageSearchButton.addEventListener('click', function() {
      uploadArea.style.display = 'none';
      searchArea.style.display = 'block';
    });
  
    // Show the upload when clicked
    imageUploadButton.addEventListener('click', function() {
      searchArea.style.display = 'none';
      uploadArea.style.display = 'block';
    });
    //submit button
    submitButton.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent form submission
  
      const file = imageUploadInput.files[0];
      // Your submit logic here
      console.log('Submit button clicked');

      if (file) {
          // Display the uploaded image
          const reader = new FileReader();
          reader.onload = function(e) {
              uploadedImageDiv.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image"">`;
          };
          reader.readAsDataURL(file);

          const formData = new FormData();
          formData.append('image', file);

          fetch('/identify', {
              method: 'POST',
              body: formData
          })
          .then(response => response.json())
          .then(data => {
              if (data.plant) {
                  resultsDiv.innerHTML = `<p>Plant Identified: <strong>${data.plant}</strong></p>`;
              } else if (data.error) {
                  resultsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
              }
          })
          .catch(error => {
              console.error('Error:', error);
              resultsDiv.innerHTML = '<p>An error occurred during plant identification.</p>';
          });
      } else {
          resultsDiv.innerHTML = '<p>Please select an image.</p>';
      }
  });
  });

//Searcg javascript

//plant data
const Plants = [
  { name: 'Violet', image: 'plant-images/flower-violet.jpg' },
  { name: 'Daisy', image: 'plant-images/flower-daisy.jpg' },
  { name: 'Orchid', image: 'plant-images/flower-orchid.jpg' },
  // ... more flowers eventually
];
//filter
function filterPlants(query) {
  return Plants.filter(plant => {
      const lowerCaseQuery = query.toLowerCase();
      return (
          plant.name.toLowerCase().includes(lowerCaseQuery)
           );
  }).sort((a, b) => a.name.localeCompare(b.name));
}

//search hangler
function searchHandler(event) {
  event.preventDefault();
  const query = document.getElementById('search-input').value.toLowerCase();
  console.log("Search Query:", query);

  // Filter the plants based on the query
  const results = filterPlants(query);

  // Display the filtered results
  displayResults(results);
}

//display search result
function displayResults(results) {
  console.log("Results to display:", results);
  const resultsContainer = document.getElementById('search-results');

  // Clear previous results
  resultsContainer.innerHTML = '';

  if (results.length === 0) {
    resultsContainer.innerHTML = '<p>No matching plant found.</p>';
    return;
  }

  results.forEach((plant) => {
    const img = document.createElement('img');
    img.src = plant.image; 
    img.alt = plant.name;
    img.style.maxWidth = '200px'; 
    img.style.margin = '10px';

    resultsContainer.appendChild(img);
  });
}


//event listhererw for search
document.getElementById('search-form').addEventListener('submit', searchHandler);

init();