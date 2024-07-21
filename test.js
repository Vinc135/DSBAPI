const jsonfile = require('jsonfile');
const moment = require('moment');
const simpleGit = require('simple-git');
const FILE_PATH = './data.json';

// Dynamischen Import für das ES-Modul
const randomPromise = import('random');

const makeCommit = async (n) => {
    if (n === 0) return simpleGit().push();
    
    // Warte auf die Import-Referenz
    const { int } = (await randomPromise).default;
    
    const x = int(0, 54);
    const y = int(0, 6);
    const DATE = moment().subtract(1, 'y').add(1, 'd').add(x, 'w').add(y, 'd').format();
    const data = { date: DATE };
    
    console.log(DATE);
    
    jsonfile.writeFile(FILE_PATH, data, () => {
        simpleGit().add([FILE_PATH]).commit(DATE, { '--date': DATE }, () => {
            makeCommit(--n);
        });
    });
};

makeCommit(100);
