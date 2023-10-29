document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById('sidebar');
    const toggleButton = document.getElementById('toggleButton');
    const submitButton = document.getElementById('submit-button');
    const messagesContainer = document.getElementById('messages');

    toggleButton.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    const data = {
        soilTypes: ['Clay', 'Loam', 'Sand'],
    };

    const soilTypeDropdown = document.getElementById('soilType');
    data.soilTypes.forEach(soilType => {
        const option = document.createElement('option');
        option.value = soilType;
        option.textContent = soilType;
        soilTypeDropdown.appendChild(option);
    });

    submitButton.addEventListener('click', async () => {
        const location = document.getElementById('location').value;
        const temperature = document.getElementById('temperature').value;
        const precipitation = document.getElementById('precipitation').value;
        const demand = document.getElementById('demand').value;
        const supply = document.getElementById('supply').value;
        const marketPrice = document.getElementById('marketPrice').value;
        const soilType = soilTypeDropdown.value;

        const data = {
            location,
            temperature,
            precipitation,
            demand,
            supply,
            marketPrice,
            soilType
        };

        const response = await fetch('/farming-decision/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();

        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.textContent = result.reply;
        messagesContainer.appendChild(messageElement);
        scrollToBottom();
    });

    document.getElementById('aiIcon').addEventListener('click', () => {
        const chatbox = document.getElementById('chatbox');
        chatbox.classList.toggle('open');
    });

    function scrollToBottom() {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
});
