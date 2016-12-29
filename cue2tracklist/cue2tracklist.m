function cue2tracklist(filepath)
fID = fopen(filepath, 'r');

regexpattern = '[ ]{1,}TITLE \"(.*?)\"';
tracklist = {};
while ~feof(fID)
    tline = fgetl(fID);
    test = regexp(tline, regexpattern, 'Tokens');
    if ~isempty(test)
        tracklist(end+1) = test{1}(1);
    end
end

fclose(fID);

fprintf('Track Listing:\n\n')
for ii = 1:length(tracklist)
    fprintf('[#] %s\n', tracklist{ii})
end

end