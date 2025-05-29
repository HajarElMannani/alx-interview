#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
if (!id) {
    process.exit(1);
}
const furl = 'https://swapi-api.alx-tools.com/${id}';
request(furl, {json: true}, (err, res, body) => {
    if (err) {
	return;
    }
    if(res.statusCode != 200) {
	return;
    }
    const charact = body.characters;
    if (!charact || !charact.length) {
	return;
    }
    (async () => {
	for (const url of charact) {
	    await new Promise((resolve, reject) => {
		request(url, {json: true}, (err, res, body) => {
		    if (err) {
			return resolve();
		    }
		    if (res.statusCode != 200) {
			return resolve();
		    }
		    console.log(body.name);
		    resolve();
		});
	    });
	}
    })();
});
