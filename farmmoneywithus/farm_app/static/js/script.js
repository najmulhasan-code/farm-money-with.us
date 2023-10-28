document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById('sidebar');
    const toggleButton = document.getElementById('toggleButton');

    toggleButton.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    const data = {
        locations: ['Tundra', 'Plains'],
        soilTypes: ['Clay', 'Loam', 'Sand'],
    };

    const locationDropdown = document.getElementById('location');
    data.locations.forEach(location => {
        const option = document.createElement('option');
        option.value = location;
        option.textContent = location;
        locationDropdown.appendChild(option);
    });

    const soilTypeDropdown = document.getElementById('soilType');
    data.soilTypes.forEach(soilType => {
        const option = document.createElement('option');
        option.value = soilType;
        option.textContent = soilType;
        soilTypeDropdown.appendChild(option);
    });
});
