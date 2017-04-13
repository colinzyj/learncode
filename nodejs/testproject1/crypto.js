'use strict';

const crypto = require('crypto');
const hash = crypto.createHash('sha256');
const hmac = crypto.createHmac('sha256','secret-key')

//hash.update('Hello,world');
//hmac.update('Hello,world')

//console.log(hash.digest('hex'));
//console.log(hmac.digest('hex'));
function aesEncrypt(data,key){
    const cipher=crypto.createCipher('aes192',key);
    var crypted = cipher.update(data,'utf-8','hex');
    crypted += cipher.final('hex')
    return crypted;
}

function aesDecrypt(encrypted, key) {
    const decipher = crypto.createDecipher('aes192', key);
    var decrypted = decipher.update(encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
}

var data = "hello";
var key='keystring';    
var encrypted = aesEncrypt(data,key);
var decrypted = aesDecrypt(encrypted,key);

console.log("data:"+data);
console.log("Encrypted:"+encrypted);
console.log("Decrypted:"+decrypted);