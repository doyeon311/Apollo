start_hour, start_min, start_sec = map(int, input().split())
sec = int(input())

end_hour, end_min, end_sec = [0, 0, 0]

end_sec = (start_sec + sec) % 60
to_min = (start_sec + sec) // 60
end_min = (start_min + to_min) % 60
to_hour = (start_min + to_min) // 60
end_hour = (start_hour + to_hour) % 24

print(end_hour, end_min, end_sec)