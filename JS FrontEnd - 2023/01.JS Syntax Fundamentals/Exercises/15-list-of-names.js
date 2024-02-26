function sortNames(namesArray) {
    return namesArray
        .sort((a,b) => a.localeCompare(b))
        .map((el,index) => `${index+1}.${el}`)
        .join('\n');
    }

console.log(sortNames(["John", "bob", "Christina", "Ema"]));

function solve(names) {
// localcompare (str,lang,options as object) -> -1(after), 0(same), +1(before)
     names.sort((a,b) => a.localeCompare(b,'en-US-u-kf-upper')) 

    for (const [index,name] of names.entries()) {
        console.log(`${index+1}.${name}`)
    } 

}

solve(["job", "Job", "Christina", "Ema"]);