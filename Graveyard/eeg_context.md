Event context (as more reliably retrieved from the 'EEG.urevent' table)
can be valuable in data analysis. For example, one may want to study all
events of a certain type (or set of types) that precede or follow events
of some other types by delays within a given range. A classic ERP
example was the demonstration by [Squires et
al.](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=64341)
that the P300 peak was larger when a rare stimulus followed a string of
standard stimuli than when it followed other rare stimuli. The (v4.4)command-line function [eeg_context.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_context.m) looks for events of
specified *target* type(s), then for preceding and/or succeeding events
of specified *neighbor* type(s).

The script below is a simple demonstration script using [eeg_context.m](http://sccn.ucsd.edu/eeglab/locatefile.php?file=eeg_context.m) that finds target events in the sample dataset

that are followed by appropriate button press responses. Some response
ambiguity is resolved by making sure the response does not follow a
succeeding target. (In that case, we assume the response is to the
second target). It also finds the responded targets that follow a
non-responded target since, we expect, the EEG dynamics time-locked to
these targets may differ in some way from those not following a 'miss'.

``` matlab
% For each target 'square' event, find the succeeding 'rt' and 'square' events

[targsrt,nextrts,nxtypert,rtlats] = eeg_context(EEG,{'square'},{'rt'},1);  % find succeeding rt events
[targssq,nextsqs,nxtypesq,sqlats] = eeg_context(EEG,{'square'},{'square'},1);  % find succeeding square events

% find target 'square' events with appropriate button-press responses

selev = []; % selected events
rejev = [];  % rejected events
for e=1:length(targsrt) % For each target,
    if rtlats(e) > 200 & rtlats(e) < 1500 ...  % if 'rt' latency in acceptable range
    & (sqlats(e) > rtlats(e) | isnan(sqlats(e))) % and no intervening 'square' event,
        selev = [selev targsrt(e,1)];  % mark target as responded to
    else  % Note: the isnan() test above tests for NaN value
    % of sqlats (when no next "square")
        rejev = [rejev targsrt(e,1)];
    end
end
rts = rtlats(selev); % collect RT latencies of responded targets
whos rtlats sqlats nextrts nextsqs
selev = targs(selev); % selev now holds the selected EEG.event numbers
rejev = targs(rejev);
fprintf(['Of %d "square" events, %d had acceptable "rt" responses ',...
'not following another "square".\n'],length(targsrt),length(selev));

%
% find targets following non-responded targets
%
aftererr = rejev+1;  % find target events following an unresponded target
aftererr(find(ismember(aftererr,selev)==0)) = [];  % remove events themselves
% not responded
whos selev rejev aftererr
fprintf(['Of %d "square" events following non-responded targets, ',...
'%d were themselves responded.\n\n'], length(rejev), length(aftererr));
```
