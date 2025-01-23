import pygame
import random
import sys
import math
import numpy as np
from queue import PriorityQueue 
from main import GRID_SIZE
from main import OBSTACLE
from main import SAND
from main import WATER
from main import MUD


class uniformCostSearch:
        
        def __init__(self, grid):
            self.grid  = grid
        
        def dijkstra_algorithm(self, start,goal):
            frontier = PriorityQueue()
            frontier.put((start,0))
            came_from = dict()
            cost_so_far = dict()
            came_from[start] = None
            cost_so_far[start] = 0

            while not frontier.empty():
                current,current_cost = frontier.get()

                if current == goal:
                    break
                for neighbor in self.get_neighbors(current):
                     new_cost = self.get_cost(current) + self.get_cost(neighbor)

                     if(neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                          cost_so_far[neighbor]=new_cost
                          priority= new_cost
                          frontier.put((neighbor,priority))
                          came_from[neighbor]= current
                return came_from, cost_so_far

        def get_neighbors(self, position):
            x, y = position
            neighbors = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                nx = dx + x
                ny = dy + y

                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.grid[ny][nx] != OBSTACLE:
                    neighbors.append((nx, ny))
            
            return neighbors
        
        def get_cost(self,position):
             x,y=position
             if(self.grid[y][x]==SAND):
                  return 1
             elif(self.grid[y][x]==MUD):
                  return 5
             elif(self.grid[y][x]==WATER):
                  return 10
