DECEMBER = '12'
lowest_temp = 0.0
date = '01.01.2015'

File.open('temperature.txt').each do |line|
  line_array =  line.split(' ')
  temp = line_array[3].sub!(',','.').to_f
  current_date = line_array[1]
  month = current_date.split('.')[1]

  if (DECEMBER == month) && (lowest_temp > temp)
    lowest_temp =  temp
    date = current_date
  end
end

p lowest_temp, date
