from pandas import read_csv

CHUNK_SIZE = 2000000

ratings = read_csv('ratings.csv')

ratings.iloc[0:CHUNK_SIZE].to_csv('ratings01.csv', index=False)
ratings.iloc[CHUNK_SIZE:(2 * CHUNK_SIZE)].to_csv('ratings02.csv', index=False)
ratings.iloc[(2 * CHUNK_SIZE):(3 * CHUNK_SIZE)].to_csv('ratings03.csv', index=False)
ratings.iloc[(3 * CHUNK_SIZE):(4 * CHUNK_SIZE)].to_csv('ratings04.csv', index=False)
ratings.iloc[(4 * CHUNK_SIZE):(5 * CHUNK_SIZE)].to_csv('ratings05.csv', index=False)
ratings.iloc[(5 * CHUNK_SIZE):(6 * CHUNK_SIZE)].to_csv('ratings06.csv', index=False)
ratings.iloc[(6 * CHUNK_SIZE):(7 * CHUNK_SIZE)].to_csv('ratings07.csv', index=False)
ratings.iloc[(7 * CHUNK_SIZE):(8 * CHUNK_SIZE)].to_csv('ratings08.csv', index=False)
ratings.iloc[(8 * CHUNK_SIZE):(9 * CHUNK_SIZE)].to_csv('ratings09.csv', index=False)
ratings.iloc[(9 * CHUNK_SIZE):20000263].to_csv('ratings10.csv', index=False)
