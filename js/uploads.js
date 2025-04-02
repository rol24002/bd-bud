// Java Script for the Uploads Page

//java to do the appearing and disappearing of the upload and search area
//Event Listner
document.addEventListener('DOMContentLoaded', function() {
    const imageSearchButton = document.querySelector('.button-group button:nth-child(1)');
    const imageUploadButton = document.querySelector('.button-group button:nth-child(2)');
    const uploadArea = document.querySelector('.upload-area');
    const searchArea = document.querySelector('.search-area');
  
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