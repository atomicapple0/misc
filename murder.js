/**
 * Searches wordplay for crossword clues and contraints.
 * 
 * @param {string} input A crossword clue
 * @param {string} input (optional) A crossword constraint matching [A-Za-z?]+ or an enumeration (length).
 * @return {string} A list of words matching the given clue (and constraint).
 *
 * @customfunction
 */
function MURDER(clue, constraint) {
 
    var pattern = '';
    
    if (typeof constraint == "undefined") {
      // do nothing
    } else if (!isNaN(parseInt(constraint, 10))) { // enumeration    
      for (var i = 0; i < parseInt(constraint, 10); i++) {
        pattern += '?'; 
      }
    } else {
      pattern = constraint.replace(/_/g, "?").trim();
    }
    
  
    var form_data = {
      'clue': clue,
      'pattern': pattern
    }
    
    var options = {
      'method' : 'post',
      'payload' : form_data,
  //    'muteHttpExceptions': true
    };
    
    // lock the script to prevent spamming wordplays and getting 503'd
    var lock = LockService.getScriptLock();
    lock.waitLock(10000); // 10 seconds
    
    const wordplays = 'https://www.wordplays.com/crossword-solver/' + encodeURIComponent(clue);
    const response = UrlFetchApp.fetch(wordplays, options)
    var responseCode = response.getResponseCode();
    
    if(responseCode == "503") {
     return "server timed out."
    }
    
    
    const html = response.getContentText();
    
    
    console.log(responseCode, html); 
    var doc = Xml.parse(html, true);
    var bodyHtml = doc.html.body.toXmlString();
    doc = XmlService.parse(bodyHtml);
    
    var root = doc.getRootElement();
      
    var table = getElementsByClassName(root, 'wp-widget-content')[0];
    if(typeof table == "undefined") {
     return "no answers found"; 
      
    }
     
    var rows = getElementsByTagName(table, 'tr');
    var rows_n = rows.length;
    
    var answers = []
    
    for (var i = 1; i < rows_n; i++) {
      var answer = getElementsByTagName(rows[i], 'td')[1].getValue() // second col contains answer
      
      answers.push(answer);
    }
    
    //console.log(answers[0].getValue());
    //var test_out = XmlService.getRawFormat().format(answers[0]);
    // the goods are in .wp-widget-content
    
    //console.log(test_out);
    return answers.join(' | ');
  }