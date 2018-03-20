# Send Asterisk CEL data to Elastic

## Prerequisite

Configure **cel_custom.conf** file adding a new mapper as follow:

	[mappings]
	Master.json => {"asterisk_ident": "lab", ${CSV_QUOTE(eventtype)}: ${CSV_QUOTE(${eventtype})}, ${CSV_QUOTE(eventtime)}: ${eventtime}, ${CSV_QUOTE(callerid_name)}: ${CSV_QUOTE(${CALLERID(name)})}, ${CSV_QUOTE(callerid_num)}: ${CSV_QUOTE(${CALLERID(num)})}, ${CSV_QUOTE(callerid_ani)}: ${CSV_QUOTE(${CALLERID(ANI)})}, ${CSV_QUOTE(callerid_dnid)}: ${CSV_QUOTE(${CALLERID(DNID)})}, ${CSV_QUOTE(channel_exten)}: ${CSV_QUOTE(${CHANNEL(exten)})}, ${CSV_QUOTE(channel_context)}: ${CSV_QUOTE(${CHANNEL(context)})}, ${CSV_QUOTE(channel_channame)}: ${CSV_QUOTE(${CHANNEL(channame)})}, ${CSV_QUOTE(channel_appname)}: ${CSV_QUOTE(${CHANNEL(appname)})}, ${CSV_QUOTE(channel_appdata)}: ${CSV_QUOTE(${CHANNEL(appdata)})}, ${CSV_QUOTE(channel_amaflags)}: ${CSV_QUOTE(${CHANNEL(amaflags)})}, ${CSV_QUOTE(channel_accountcode)}: ${CSV_QUOTE(${CHANNEL(accountcode)})}, ${CSV_QUOTE(channel_uniqueid)}: ${CSV_QUOTE(${CHANNEL(uniqueid)})}, ${CSV_QUOTE(channel_linkedid)}: ${CSV_QUOTE(${CHANNEL(linkedid)})}, ${CSV_QUOTE(bridgepeer)}: ${CSV_QUOTE(${BRIDGEPEER})}, ${CSV_QUOTE(channel_userfield)}: ${CSV_QUOTE(${CHANNEL(userfield)})}, ${CSV_QUOTE(userdeftype)}: ${CSV_QUOTE(${userdeftype})}, ${CSV_QUOTE(eventextra)}: '${eventextra}'}

## Usage
```console
$ docker run -d --name cel_to_es --restart always \
    -v /etc/ssl/certs:/etc/ssl/certs:ro \
    -v /var/log/asterisk/cel-custom:/data:ro \
    -v /var/tmp/cel:/tmp \
    vacolba/asterisk-cel-es:0.0.2 --es https://es.example.com /data/Master.json
```

### Volumes

| Mount Point    | Description            |
|----------------|------------------------|
| /etc/ssl/certs | SSL certs  			  |
| /data          | CEL data file location |
| /tmp     		 | Store position file    |
