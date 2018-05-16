%% plot_bode: plot frequency response of transfer function
% sys: transfer function
% freqs: frequency to be plot
% varargin: other parameters
% 	'DisplayName': Legend show
%	'LineWidth': line width
%	'Color': color of line

function plot_bode(sys,freqs,varargin)
resp=squeeze(freqresp(sys,2*pi*freqs));
mag=20*log10(abs(resp));
phs=angle(resp)*180/pi;

subplot(211);mag_h=semilogx(freqs,mag);
grid on;hold on;
xlim([freqs(1),freqs(end)]);

subplot(212);phs_h=semilogx(freqs,phs);
grid on;hold on;
xlim([freqs(1),freqs(end)]);

% set options of line
index = findIndex(varargin,'DisplayName');
if(index>0)
    set(mag_h,'DisplayName',varargin{index+1});
    set(phs_h,'DisplayName',varargin{index+1});
end

% set line width
index = findIndex(varargin,'LineWidth');
if(index>0)
    set(mag_h,'LineWidth',varargin{index+1});
    set(phs_h,'LineWidth',varargin{index+1});
end

% set line color
index = findIndex(varargin,'Color');
if(index>0)
    set(mag_h,'Color',varargin{index+1});
    set(phs_h,'Color',varargin{index+1});
end


end

function y=findIndex(args,optionName)

y=-1;
for i=1:numel(args)
    if(strcmp(args{i},optionName))
        y=i;
        break;
    end
end

end
