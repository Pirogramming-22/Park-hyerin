let time = 0; 
let running = false; 
let interval; 
let selectedRecords = []; 

const timeDisplay = document.querySelector('.time');
const startButton = document.querySelector('.start');
const stopButton = document.querySelector('.stop');
const resetButton = document.querySelector('.reset');
const recordsList = document.querySelector('.records');
const checkboxIcon = document.querySelector('.ri-checkbox-blank-circle-line');
const deleteIcon = document.querySelector('.ri-delete-bin-7-line');
const recordCheckboxes = [];

const formatTime = (ms) => {
    const minutes = Math.floor(ms / 60000);
    const seconds = Math.floor((ms % 60000) / 1000);
    const milliseconds = Math.floor(ms % 1000 /10);

    return minutes > 0 
        ? `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}:${String(milliseconds)}`
        : `${String(seconds).padStart(2, '0')}:${String(milliseconds)}`;
};

const startStopwatch = () => {
    if (!running) {
        interval = setInterval(() => {
            time += 10; // Increment time by 10ms
            timeDisplay.textContent = formatTime(time);
        }, 10);
        running = true;
    } 
};

const stopStopwatch = () => {
    if (running) {
        clearInterval(interval);
        running = false;
        startButton.textContent = 'start';
    }
    
    // Add record
    const record = document.createElement('li');
    record.classList.add('record');
    const recordText = document.createElement('span');
    recordText.textContent = formatTime(time);
    const recordCheckbox = document.createElement('i');
    recordCheckbox.classList.add('ri-checkbox-blank-circle-line');
    recordCheckbox.addEventListener('click', () => toggleRecordSelection(recordCheckbox, record));
    
    record.appendChild(recordCheckbox);
    record.appendChild(recordText);
    recordsList.appendChild(record);
};

const resetStopwatch = () => {
    time = 0;
    timeDisplay.textContent = '00:00';
    if (running) {
        clearInterval(interval);
        running = false;
        startButton.textContent = 'start';
    }
};

const toggleRecordSelection = (checkbox, record) => {
    const index = selectedRecords.indexOf(record);
    if (index === -1) {
        selectedRecords.push(record);
        checkbox.classList.replace('ri-checkbox-blank-circle-line', 'ri-checkbox-circle-line');
    } else {
        selectedRecords.splice(index, 1);
        checkbox.classList.replace('ri-checkbox-circle-line', 'ri-checkbox-blank-circle-line');
    }
};


const toggleAllRecordSelection = () => {
    const allChecked = checkboxIcon.classList.contains('ri-checkbox-circle-line');
    
    if (allChecked) {
        selectedRecords = [];
        checkboxIcon.classList.replace('ri-checkbox-circle-line', 'ri-checkbox-blank-circle-line');
        recordsList.querySelectorAll('.record').forEach((record) => {
            const recordCheckbox = record.querySelector('i');
            recordCheckbox.classList.replace('ri-checkbox-circle-line', 'ri-checkbox-blank-circle-line');
        });
    } else {
        selectedRecords = Array.from(recordsList.querySelectorAll('.record'));
        checkboxIcon.classList.replace('ri-checkbox-blank-circle-line', 'ri-checkbox-circle-line');
        recordsList.querySelectorAll('.record').forEach((record) => {
            const recordCheckbox = record.querySelector('i');
            recordCheckbox.classList.replace('ri-checkbox-blank-circle-line', 'ri-checkbox-circle-line');
        });
    }
};

const deleteSelectedRecords = () => {
    selectedRecords.forEach((record) => {
        recordsList.removeChild(record);
    });
    selectedRecords = [];
    
    checkboxIcon.classList.replace('ri-checkbox-circle-line', 'ri-checkbox-blank-circle-line');
};

startButton.addEventListener('click', startStopwatch);
stopButton.addEventListener('click', stopStopwatch);
resetButton.addEventListener('click', resetStopwatch);
checkboxIcon.addEventListener('click', toggleAllRecordSelection);
deleteIcon.addEventListener('click', deleteSelectedRecords);
