document.addEventListener('DOMContentLoaded', function() {
  var cinemaSelect = document.getElementById('cinemaSelect');
  var showtimesContainer = document.getElementById('showtimes-container');

  // This function updates the showtimes when a cinema is selected
  function updateShowtimes(cinema) {
      // Clear existing showtimes
      showtimesContainer.innerHTML = '';

      // Here you would typically get these showtimes from a server or define them for each cinema
      var showtimes = {
          'mlociny': ['10:00', '10:50', '11:50', '12:35', '13:40', '14:40', '15:30', '16:30', '17:30', '19:20', '20:20'],
          // Add showtimes for other cinemas as needed
      };
    // Check if the selected cinema has showtimes defined
    if (showtimes[cinema]) {
        // Loop over the showtimes and create elements for each
        showtimes[cinema].forEach(function(time) {
            var showtimeDiv = document.createElement('div');
            showtimeDiv.className = 'showtime';
            showtimeDiv.textContent = time;
            showtimesContainer.appendChild(showtimeDiv);
        });
    }
    }

    // Add an event listener to the select element
    cinemaSelect.addEventListener('change', function() {
    updateShowtimes(this.value);
    });

    // Initialize with the first cinema's showtimes
    updateShowtimes(cinemaSelect.value);
    });
