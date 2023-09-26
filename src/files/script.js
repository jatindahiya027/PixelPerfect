const { PythonShell } = require("python-shell");
const path = require('path');

function compressimg(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
  const slide = document.getElementById("slider")
  console.log(slide.value)
  const depth = document.getElementById("depth")
  console.log(depth.value)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [JSON.stringify(filePaths),depth.value,slide.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("compressimg.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
function compressfolder(){
  
  const path = document.getElementById("inputpath")
  console.log(path.value)
 
  const slide = document.getElementById("slider")
  console.log(slide.value)
  const depth = document.getElementById("depth")
  console.log(depth.value)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [path.value,depth.value,slide.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("compressimgfolder.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
function resizeimg(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
  const width = document.getElementById("width")
  console.log(width.value)
  const height = document.getElementById("height")
  console.log(height.value)
  const depth = document.getElementById("depth")
  console.log(depth.value)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [JSON.stringify(filePaths),width.value,height.value,depth.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("resizeimage.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
function resizefolder(){
  const path = document.getElementById("inputpath")
  console.log(path.value)
  const width = document.getElementById("width")
  console.log(width.value)
  const height = document.getElementById("height")
  console.log(height.value)
  const depth = document.getElementById("depth")
  console.log(depth.value)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [path.value,width.value,height.value,depth.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("resizeimagefolder.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
function convertimg(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
 
  const format = document.getElementById("depth")
  console.log(format.value)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [JSON.stringify(filePaths),format.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("convertimg.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
function convertfolder(){
  
  const path = document.getElementById("inputpath")
  console.log(path.value)
 
  const format = document.getElementById("depth")
  console.log(format.value)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [path.value,format.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("convertimgfolder.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
function vidtogif(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
 
  // output= "C:/Users/91741/Downloads/one.gif"
  showPopup();
  for( pathh in filePaths ){
    
    console.log(pathh)
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [filePaths[pathh]],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("vidtogiif.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
    }
}
function vidtoaudio(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
 
  const format = document.getElementById("depth")
  console.log(format.value)
  // output= "C:/Users/91741/Downloads/one"
  showPopup();
  for( pathh in filePaths ){
   
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [filePaths[pathh],format.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("vidtoaudio.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
}
function artifactrm(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
  const slide = document.getElementById("slider")
  console.log(slide.value)
  // output= "C:/Users/91741/Downloads/out.jpg"
  showPopup();
  for( pathh in filePaths ){
    
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python/JPEG_Artifacts_Removal",
      args: [filePaths[pathh],slide.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("artifactremoval.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}}
function depthgen(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
  // output= "C:/Users/91741/Downloads/out.jpg"

  showPopup();
  for( pathh in filePaths ){
    
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [filePaths[pathh]],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("depth.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
}
function bgrem(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
 
  const format = document.getElementById("depth")
  console.log(format.value)
  showPopup();
  for( pathh in filePaths ){
   
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [filePaths[pathh], format.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("bgremove.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
}
function stylegan(){
  
  const pathh = document.getElementById("inputpath")
  console.log(pathh.value)
  const modee = document.getElementById("depth").value

  console.log(modee)
  showPopup();
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [pathh.value,modee]
    };
    let img=  document.getElementById("stylegan");
    img.src= "result.jpg"
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("stylegan.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
          
           
            img.src = pathh.value+"/result.png"
        
         


      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
     
}
function imagesr(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
  // output=  "C:/Users/91741/Downloads/New folder (6)/outttt.jpg"
  const format = document.getElementById("depth")
  console.log(format.value)
  showPopup();
  for( pathh in filePaths ){
    
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python/OmniSR",
      args: [filePaths[pathh],format.value],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("superrs.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
}
function noiserm(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
 
  // output= "C:/Users/91741/Downloads/New folder (6)/out.png"
  showPopup();
  for( pathh in filePaths ){
    
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python/denoise",
      args: [filePaths[pathh]],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("denoiseimg.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
}

function audiodenoise(){
  
  if(filePaths.length === 0){
     
    return;
  }
  console.log(filePaths)
 
  
  showPopup();
  for( pathh in filePaths ){
    
    const options = {
      mode: "text",
      pythonPath: "C:/ProgramData/miniconda3/python.exe", // Replace with the path to your Python executable if necessary
      scriptPath: "C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python",
      args: [filePaths[pathh]],
    };
  
    let successMessageReceived = false; // To track if success message is received
    PythonShell.run("denoiseaudio.py", options)
      .then((results) => {
          console.log(results)
          closePopup();
          showPopupsuccess()
      })
      .catch((err) => {
        console.error("Error:", err);
        closePopup();
        showPopuperror()
      });
}
}










function showPopup() {
  // Create the popup container element
  var popupContainer = document.createElement('div');
  popupContainer.classList.add('popup-container');

  // Create the loader
  var loader = document.createElement('div');
  loader.classList.add('lds-spinner');
  loader.innerHTML = '<div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>';

  // Create the "Processing..." text
  var processingText = document.createElement('div');
  processingText.classList.add('popup-text');
  processingText.textContent = 'Processing...';

  // Create the OK button
  // var okButton = document.createElement('button');
  // okButton.classList.add('ok-button');
  // okButton.textContent = 'OK';
  // okButton.addEventListener('click', closePopup);

  // Append loader, text, and button to the popup container
  popupContainer.appendChild(loader);
  popupContainer.appendChild(processingText);
  // popupContainer.appendChild(okButton);

  // Append the popup container to the body
  document.body.appendChild(popupContainer);

  // Display the popup
  popupContainer.style.display = 'flex';
  popupContainer.style.flexDirection='column';
}

function showPopupsuccess() {
// Create the popup container element
var popupContainer = document.createElement('div');
popupContainer.classList.add('popup-container');

// Create the loader
var loader = document.createElement('div');

loader.innerHTML = '<p>Sucessfully completed the task</p>';

// Create the "Processing..." text
// var processingText = document.createElement('div');
// processingText.classList.add('popup-text');
// processingText.textContent = 'Processing...';

// Create the OK button
var okButton = document.createElement('button');
okButton.classList.add('ok-button');
okButton.textContent = 'OK';
okButton.style.width="100px"
okButton.style.height="40px"
okButton.style.borderRadius="10px"
okButton.style.border="none"
okButton.style.fontWeight="500"
okButton.style.cursor="pointer"
okButton.addEventListener('click', closePopup);

// Append loader, text, and button to the popup container
popupContainer.appendChild(loader);
// popupContainer.appendChild(processingText);
popupContainer.appendChild(okButton);

// Append the popup container to the body
document.body.appendChild(popupContainer);

// Display the popup
popupContainer.style.display = 'flex';
popupContainer.style.flexDirection='column';
}
function showPopuperror() {
  // Create the popup container element
  var popupContainer = document.createElement('div');
  popupContainer.classList.add('popup-container');

  // Create the loader
  var loader = document.createElement('div');
  
  loader.innerHTML = '<p>Error accoured</p>';

  // Create the "Processing..." text
  // var processingText = document.createElement('div');
  // processingText.classList.add('popup-text');
  // processingText.textContent = 'Processing...';

  // Create the OK button
  var okButton = document.createElement('button');
  okButton.classList.add('ok-button');
okButton.textContent = 'OK';
okButton.style.width="100px"
okButton.style.height="40px"
okButton.style.borderRadius="10px"
okButton.style.border="none"
okButton.style.fontWeight="500"
okButton.style.cursor="pointer"
  okButton.addEventListener('click', closePopup);

  // Append loader, text, and button to the popup container
  popupContainer.appendChild(loader);
  // popupContainer.appendChild(processingText);
  popupContainer.appendChild(okButton);

  // Append the popup container to the body
  document.body.appendChild(popupContainer);

  // Display the popup
  popupContainer.style.display = 'flex';
  popupContainer.style.flexDirection='column';

}
// Function to close the popup
function closePopup() {
  var popupContainer = document.querySelector('.popup-container');
  if (popupContainer) {
      document.body.removeChild(popupContainer);
  }
}