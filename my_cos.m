function result_cos = my_cos(in_rad, nth)

% ���������
% in_rad: ����ĽǶȣ����ȣ�
% nth: ̩�ռ���չ��������

result_cos = 0;
term = 1;
for i = 0:nth
    result_cos = result_cos + term;
    term = -term * in_rad^2 / ((2*i+1)*(2*i+2));
end

end