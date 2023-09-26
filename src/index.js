const { app, BrowserWindow ,ipcMain, dialog,Menu} = require('electron');
const fs = require('fs');
const path = require('path');
const fse = require('fs-extra');



// Handle creating/removing shortcuts on Windows when installing/uninstalling.
const sourceDirectory = path.join(__dirname, 'files/python'); // Replace with the path to your directory
const destinationDirectory = 'C:/Users/91741/AppData/Local/pixelperfect/app-1.0.0/resources/python'; // Replace with the path to your destination directory
function move(){
  fse.ensureDirSync(destinationDirectory);

fs.readdir(sourceDirectory, (err, files) => {
  if (err) {
    console.error('Error reading source directory:', err);
    return;
  }

  console.log('Copying files from source to destination directory:');
  files.forEach((file, index) => {
    const sourceFilePath = path.join(sourceDirectory, file);
    const destinationFilePath = path.join(destinationDirectory, file);

    // Use fs-extra's copySync to copy the file
    try {
      fse.copySync(sourceFilePath, destinationFilePath);
      // console.log(`Copied ${file}`);
    } catch (copyError) {
      console.error(`Error copying ${file}:`, copyError);
    }
  });
});
}
// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) {
  app.quit();
}

const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    icon: path.join(__dirname, "logo/logo.ico"),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: false, // Enable Node.js integration
    },
   
  });

  // and load the index.html of the app.
  mainWindow.loadFile(path.join(__dirname, 'index.html'));

  // Open the DevTools.
  // mainWindow.webContents.openDevTools();
  ipcMain.on('open-dialog', (event) => {
    dialog.showOpenDialog(mainWindow, {
      properties: ['openDirectory']
    }).then(result => {
      if (!result.canceled && result.filePaths.length > 0) {
        event.reply('selected-folder', result.filePaths[0]);
      }
    }).catch(err => {
      console.error('Error in openDialog:', err);
    });
  });
  mainWindow.maximize();
  Menu.setApplicationMenu(null);

  if (fs.existsSync(destinationDirectory)) {
    console.log('Folder exists.');
  } else {
    console.log('Folder does not exist.');
    move();
  }
 
};

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
