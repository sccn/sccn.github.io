function replace_file_links(fileName)

fid = fopen(fileName, 'r');
if fid == -1
    error('File not found');
end

pattern1 = { '{ {File\|' '{{File\|' };
pattern2 = { '} }' '}}' };

allStrs = {};
count   = 1;
while ~feof(fid)
    allStrs{count} = fgetl(fid);
    
    replace_txt(allStrs{count}, pattern1, pattern2);
    
    if count > 1
        [twoLines,content] = replace_txt([ allStrs{count-1} allStrs{count} ], pattern1, pattern2);
        if ~isempty(content)
            allStrs{count-1} = twoLines;
            allStrs{count} = '';
        end
    end
    count = count+1;
end
fclose(fid);    

% write new file
fid = fopen('test.md', 'w');
for iRow = 1:length(allStrs)
    fprintf(fid, '%s\n', allStrs{iRow});
end
fclose(fid);    

function [twoLines, content] = replace_txt(twoLines, pattern1, pattern2)

indB1 = strfind(twoLines, pattern1{1}); indPat1 = 1;
indB2 = strfind(twoLines, pattern2{1}); indPat2 = 1;
content = '';
if isempty(indB1), indB1 = strfind(twoLines, pattern1{2}); indPat1 = 2; end
if isempty(indB2), indB2 = strfind(twoLines, pattern2{2}); indPat2 = 2; end
if ~isempty(indB1) && ~isempty(indB2)
    content = twoLines(indB1+length(pattern1{indPat1}):indB2-1);
    fprintf('Found: %s\n', content);
    twoLines = [ twoLines(1:indB1-1) '[' content '](http://sccn.ucsd.edu/eeglab/locatefile.php?file=' content ')' twoLines(indB2+length(pattern2{indPat2}):end) ];
end
