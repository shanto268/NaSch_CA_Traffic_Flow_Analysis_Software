function y = piecewiseLine(x,a,b,c,d,k)

% PIECEWISELINE   A line made of two pieces
% that is not continuous.

y = zeros(size(x));

% This example includes a for-loop and if statement
% purely for example purposes.
for i = 1:length(x)
    if x(i) < k,
        y(i) = a + b.* x(i);
    else
        y(i) = c + d.* x(i);
    end
end
end
x = [0.81;0.91;0.13;0.91;0.63;0.098;0.28;0.55;...
    0.96;0.96;0.16;0.97;0.96];
y = [0.17;0.12;0.16;0.0035;0.37;0.082;0.34;0.56;...
    0.15;-0.046;0.17;-0.091;-0.071];
cftool
