function test_cputime(block)
% Level-2 MATLAB file S-Function for times two demo.
%   Copyright 1990-2009 The MathWorks, Inc.

  setup(block);
  
%endfunction

function setup(block)

global block_pre_cputime block_du_time block_diff_time
  
  %% Register number of input and output ports
  block.NumInputPorts  = 2;
  block.NumOutputPorts = 2;

  %% Setup functional port properties to dynamically
  %% inherited.
 block.SetPreCompInpPortInfoToDynamic;
 block.SetPreCompOutPortInfoToDynamic;
  block.InputPort(1).Complexity   = 'Real'; 
  block.InputPort(1).DataTypeId   = 0;
  block.InputPort(1).SamplingMode = 'Sample';
  block.InputPort(1).Dimensions   = 1;
  
  block.InputPort(2).Complexity   = 'Real';
  block.InputPort(2).DataTypeId   = 0;
  block.InputPort(2).SamplingMode = 'Sample';
  block.InputPort(2).Dimensions   = 1;
  
  block.OutputPort(1).Complexity   = 'Real';
  block.OutputPort(1).DataTypeId   = 0;
  block.OutputPort(1).SamplingMode = 'Sample';
  block.OutputPort(1).Dimensions   = 1;

  block.OutputPort(2).Complexity   = 'Real';
  block.OutputPort(2).DataTypeId   = 0;
  block.OutputPort(2).SamplingMode = 'Sample';
  block.OutputPort(2).Dimensions   = 1;
%  block.InputPort(1).DirectFeedthrough = true;
  
  %% Set block sample time to inherited
  block.SampleTimes = [-1 0];
  
  %% Set the block simStateCompliance to default (i.e., same as a built-in block)
  block.SimStateCompliance = 'DefaultSimState';

  %% Run accelerator on TLC
  block.SetAccelRunOnTLC(true);
  
  %% Init user-define properties
  block_pre_cputime=-1;
  block_du_time=0;
  block_diff_time=0;
  %% Register methods
  block.RegBlockMethod('Outputs',                 @Output);  
  
%endfunction

function Output(block)
global block_pre_cputime block_du_time block_diff_time
if (block_pre_cputime<0)
    block_pre_cputime=cputime();
    block_du_time=0;
    block_diff_time=0;
    block.OutputPort(1).Data = 0;
    block.OutputPort(2).Data = 0;
else
    tmp=cputime();
    block_du_time=block_du_time+tmp-block_pre_cputime;
    block_diff_time=block_diff_time+tmp-block_pre_cputime;
    if(block_diff_time>block.InputPort(1).Data)  
        block.OutputPort(1).Data = 1;
        block_diff_time=block_diff_time-block.InputPort(1).Data;
    else
        block.OutputPort(1).Data = 0;
    end
    if(block_du_time>block.InputPort(2).Data)
        block.OutputPort(2).Data=1;
    end
    block_pre_cputime=tmp;
  
end
  
%endfunction

