let randomNumbers = [];
let attempts = 9; 

document.getElementById('attempts').textContent = attempts;

function generateRandomNumbers() {
    while (randomNumbers.length < 3) {
        const number = Math.floor(Math.random() * 10); 
        if (!randomNumbers.includes(number)) {
            randomNumbers.push(number); 
        }
    }
}

generateRandomNumbers();
console.log(randomNumbers);

function check_numbers() {
    const input1 = document.getElementById('number1').value;
    const input2 = document.getElementById('number2').value;
    const input3 = document.getElementById('number3').value;

    if (!input1 || !input2 || !input3) {
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        return;
    }

    const userInputs = [parseInt(input1), parseInt(input2), parseInt(input3)];

    let strikeCount = 0;
    let ballCount = 0;

    userInputs.forEach((num, index) => {
        if (randomNumbers.includes(num)) {
            if (randomNumbers[index] === num) {
                strikeCount++; 
            } else {
                ballCount++; 
            }
        }
    });

 const resultsDiv = document.getElementById('results'); 
 const resultRow = document.createElement('div');
 resultRow.className = 'check-result';
 resultRow.style.display ='flex';
 resultRow.style.justifyContent ='space-between';



 const inputSpan = document.createElement('span');
 inputSpan.textContent = `${userInputs.join(' ')}`;
 inputSpan.className = 'left';
 resultRow.appendChild(inputSpan);

 const separatorSpan = document.createElement('span');
 separatorSpan.textContent = ':';
 separatorSpan.style.margin = '0 85px';
 resultRow.appendChild(separatorSpan);

 const resultContainer = document.createElement('span');
 resultContainer.className = 'right';
 //out
 if (strikeCount === 0 && ballCount === 0) {
     const outSpan = document.createElement('span');
     outSpan.className = 'out num-result';
     outSpan.textContent = 'O';
     resultContainer.appendChild(outSpan);
 } else {
        //strike
         const strikeSpan = document.createElement('span');

         const strikeNumber = document.createElement('span');
         strikeNumber.className = 'num-result';
         strikeNumber.innerHTML = `<span>${strikeCount}</span>`;
         strikeSpan.appendChild(strikeNumber);

         const strikeCircle = document.createElement('span');
         strikeCircle.className = 'strike num-result'; 
         strikeCircle.innerHTML = `S`;
         strikeSpan.appendChild(strikeCircle);

         resultContainer.appendChild(strikeSpan);

        //ball
         const ballSpan = document.createElement('span');

         const ballNumber = document.createElement('span');
         ballNumber.className = 'num-result';
         ballNumber.innerHTML = `<span>${ballCount}</span>`;
         ballSpan.appendChild(ballNumber);

         const ballCircle = document.createElement('span');
         ballCircle.className = 'ball num-result';
         ballCircle.innerHTML = `B`;
         ballSpan.appendChild(ballCircle);
         resultContainer.appendChild(ballSpan);
     
 }

 resultRow.appendChild(resultContainer);
 resultsDiv.appendChild(resultRow); 

    attempts--;
    document.getElementById('attempts').textContent = attempts;

    if (strikeCount === 3) {
        endGame(true); 
    } else if (attempts === 0) {
        endGame(false); 
    }

    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
}

function endGame(isWin) {
    const gameResultImg = document.getElementById('game-result-img');
    const submitButton = document.querySelector('.submit-button');

    if (isWin) {
        gameResultImg.src = './success.png'; 
    } else {
        gameResultImg.src = './fail.png'; 
    }

    submitButton.disabled = true; 
}

