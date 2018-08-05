patient_subpath = './180723/1185182';

filename = strcat('../strabismus_data/', patient_subpath, '/간헐적외사시_right.csv');
M = csvread(filename);
[n_rows, n_cols] = size(M);

directions = [M(:,5), M(:,6), M(:,7)];
mean_direction = mean(directions);

mean_angle = 0;
std_angle = 0;

for ii=1:n_rows
    angle = atan2(norm(cross(directions(ii, :), mean_direction)), dot(directions(ii, :), mean_direction));
    
    mean_angle = mean_angle + angle;
    std_angle = std_angle + power(angle, 2);
end

mean_angle = mean_angle / n_rows;
std_angle = power(std_angle / n_rows - power(mean_angle, 2), 0.5);

disp(patient_subpath);
disp(mean_angle);
disp(std_angle);