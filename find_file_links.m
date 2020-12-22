function find_file_links(folder)

allFiles = dir(folder);

for iFile = 1:length(allFiles)
    currentFile = fullfile(allFiles(iFile).folder, allFiles(iFile).name);
    [~,~,ext] = fileparts(allFiles(iFile).name);
    if ~(allFiles(iFile).name(1) == '.')
        if exist(currentFile, 'dir')
            find_file_links(currentFile);
        elseif isequal(lower(ext), '.md')
            scan_links(currentFile);
        end
    end
end

function scan_links(fileName)

fid = fopen(fileName, 'r');
if fid == -1
    error('File not found');
end

pattern1 = '[';
pattern2 = '](';
pattern3 = '"wikilink")';

allStrs = {};
count   = 1;
while ~feof(fid)
    allStrs{count} = fgetl(fid);
    find_txt(fileName, allStrs{count}, pattern1, pattern2, pattern3);
    
    if count > 1
        find_txt(fileName, [ allStrs{count-1} allStrs{count} ], pattern1, pattern2, pattern3);
    end
    count = count+1;
end
fclose(fid);    

function find_txt(fileName, twoLines, pattern1, pattern2, pattern3)

indB1 = strfind(twoLines, pattern1);
indB2 = strfind(twoLines, pattern2);
indB3 = strfind(twoLines, pattern3);
content = '';
if ~isempty(indB1) && ~isempty(indB2) && ~isempty(indB3)
    indB2(indB2 < indB1(1)) = [];
    
    if ~isempty(indB2)
        indB3(indB3 < indB2(1)) = [];

        if ~isempty(indB3)
            content = twoLines(indB1(1):indB3(1)+length(pattern3)-1);
            fprintf('%s: %s\n', fileName, content);
        end
    end
end
