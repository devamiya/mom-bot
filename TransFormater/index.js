const PizZip = require("pizzip");
const { DOMParser, XMLSerializer } = require("@xmldom/xmldom");
const fs = require("fs");
const path = require("path");

function str2xml(str) {
    if (str.charCodeAt(0) === 65279) {
        str = str.substr(1);
    }
    return new DOMParser().parseFromString(str, "text/xml");
}

function getParagraphs(content) {
    const zip = new PizZip(content);
    const xml = str2xml(zip.files["word/document.xml"].asText());
    const paragraphsXml = xml.getElementsByTagName("w:p");
    const paragraphs = [];

    for (let i = 0, len = paragraphsXml.length; i < len; i++) {
        let fullText = "";
        let count = 0;
        const textsXml =
            paragraphsXml[i].getElementsByTagName("w:t");
        for (let j = 0, len2 = textsXml.length; j < len2; j++) {
            const textXml = textsXml[j];
            
            if (textXml.childNodes && count!=0) {
              if(count==1){
                fullText += textXml.childNodes[0].nodeValue+': ';
              } else {
              fullText += textXml.childNodes[0].nodeValue;
              }
            }
            count++
        }
        count=0
        paragraphs.push(fullText);
    }
    return paragraphs;
}

const content = fs.readFileSync(
    path.resolve(__dirname, "Transcript_23ae87f7-ff69-402e-be6d-e05d2d7cf5c7.docx"),
    "binary"
);

console.log(getParagraphs(content));