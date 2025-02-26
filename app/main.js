/*
Input = json array


Output = HTML tabel


Check naar tijd, link de tijd met de relatieve index, krijg de info, link die naar de html dinges
*/
let raw_table;





raw_table = fetch("./schedule.txt")
document.getElementById('test').innerHTML = raw_table
console.log(raw_table)