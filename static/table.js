// Function to fetch the JSON data and populate the table
async function loadSearchHistory() {
    try {
        // Fetch the JSON file
        const response = await fetch('/history.json'); // Adjust the path if necessary
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        // Parse the JSON data
        const data = await response.json();
        
        // Get the table body element
        const tableBody = document.getElementById('searchHistoryTable').getElementsByTagName('tbody')[0];
        
        // Clear the existing rows in the table body
        tableBody.innerHTML = '';

        // Loop through each entry in the data and create table rows
        data.forEach(entry => {
            const row = tableBody.insertRow(); // Insert a new row

            // Create cells and populate them with data
            const searchTermCell = row.insertCell(0);
            const dateCell = row.insertCell(1);
            const timeCell = row.insertCell(2);

            searchTermCell.textContent = entry[0]; // Search term
            dateCell.textContent = entry[1]; // Date
            timeCell.textContent = entry[2]; // Time
        });
    } catch (error) {
        console.error('Error fetching the JSON data:', error);
    }
}

// Load the search history when the window loads
window.onload = loadSearchHistory;