import pygame
import math
import colorsys
import random


class ColorOrb:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.pulse = 0

    def update(self):
        self.pulse += 0.1
        self.radius = 10 + math.sin(self.pulse) * 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))


class Spider:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = 0
        self.max_speed = 4
        self.acceleration = 0.2
        self.leg_length = 20
        self.direction = 0
        self.target_direction = 0
        self.rotation_speed = 0.1
        self.legs = [{'angle': i * math.pi / 4, 'phase': i * math.pi / 4, 'offset': 0} for i in range(8)]
        self.body_wobble = 0
        self.color_phase = 0
        self.body_color = self.get_rainbow_color(0)

    def move(self):
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 1:
            self.target_direction = math.atan2(dy, dx)
            angle_diff = (self.target_direction - self.direction + math.pi) % (2 * math.pi) - math.pi
            if abs(angle_diff) > 0.1:
                self.direction += math.copysign(self.rotation_speed, angle_diff)
            else:
                self.direction = self.target_direction

            self.speed = min(self.speed + self.acceleration, self.max_speed)
            self.x += math.cos(self.direction) * self.speed
            self.y += math.sin(self.direction) * self.speed

            self.update_legs()
            self.body_wobble += self.speed * 0.1
            self.body_wobble %= 2 * math.pi

            self.color_phase += 0.02
            self.body_color = self.get_rainbow_color(self.color_phase)
        else:
            self.speed = 0
            self.x = self.target_x
            self.y = self.target_y

    def update_legs(self):
        for i, leg in enumerate(self.legs):
            base_angle = i * math.pi / 4
            target_angle = self.direction + base_angle
            leg['angle'] = self.lerp_angle(leg['angle'], target_angle, 0.1)
            leg['phase'] += self.speed * 0.2
            leg['phase'] %= 2 * math.pi
            leg['offset'] = math.sin(leg['phase']) * 5

    @staticmethod
    def lerp_angle(a, b, t):
        diff = (b - a + math.pi) % (2 * math.pi) - math.pi
        return a + diff * t

    @staticmethod
    def get_rainbow_color(phase):
        r, g, b = colorsys.hsv_to_rgb((phase % 1.0), 0.8, 0.8)
        return (int(r * 255), int(g * 255), int(b * 255))

    def draw(self, screen):
        body_x = self.x + math.sin(self.body_wobble) * 2
        body_y = self.y + math.cos(self.body_wobble) * 2

        pygame.draw.circle(screen, self.body_color, (int(body_x), int(body_y)), 10)

        for i, leg in enumerate(self.legs):
            leg_color = self.get_rainbow_color((self.color_phase + i * 0.125) % 1.0)

            joint_x = body_x + math.cos(leg['angle']) * self.leg_length * 0.5
            joint_y = body_y + math.sin(leg['angle']) * self.leg_length * 0.5

            end_x = joint_x + math.cos(leg['angle']) * self.leg_length * 0.5
            end_y = joint_y + math.sin(leg['angle']) * self.leg_length * 0.5 + leg['offset']

            pygame.draw.line(screen, leg_color, (body_x, body_y), (joint_x, joint_y), 2)
            pygame.draw.line(screen, leg_color, (joint_x, joint_y), (end_x, end_y), 2)

            pygame.draw.circle(screen, (255, 255, 255), (int(joint_x), int(joint_y)), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(end_x), int(end_y)), 2)

        eye_distance = 4
        eye_color = (255, 255, 255)
        pygame.draw.circle(screen, eye_color, (int(body_x - eye_distance), int(body_y - eye_distance)), 2)
        pygame.draw.circle(screen, eye_color, (int(body_x + eye_distance), int(body_y - eye_distance)), 2)

class ChromaticSpiderGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Araña Cromática: Cazadora de Colores")
        self.clock = pygame.time.Clock()
        self.spider = Spider(width // 2, height // 2)
        self.color_orbs = []
        self.score = 0
        self.level = 1
        self.time_left = 60
        self.font = pygame.font.Font(None, 36)
        self.running = False

    def spawn_color_orb(self):
        x = random.randint(20, self.width - 20)
        y = random.randint(20, self.height - 20)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.color_orbs.append(ColorOrb(x, y, color))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.spider.target_x, self.spider.target_y = pygame.mouse.get_pos()

    def update(self):
        self.spider.move()

        for orb in self.color_orbs:
            orb.update()
            if math.hypot(self.spider.x - orb.x, self.spider.y - orb.y) < 20:
                self.color_orbs.remove(orb)
                self.score += 10
                self.spawn_color_orb()

        if len(self.color_orbs) < self.level + 2:
            self.spawn_color_orb()

        self.time_left -= 1 / 60  # Disminuir en 1 segundo cada 60 frames
        if self.time_left <= 0:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.time_left = 60
        self.spider.max_speed += 0.5

    def draw(self):
        self.screen.fill((0, 0, 0, 10))

        for orb in self.color_orbs:
            orb.draw(self.screen)

        shadow_pos = (int(self.spider.x + 5), int(self.spider.y + 5))
        pygame.draw.circle(self.screen, (30, 30, 30), shadow_pos, 12)
        self.spider.draw(self.screen)

        score_text = self.font.render(f"Puntuación: {self.score}", True, (255, 255, 255))
        level_text = self.font.render(f"Nivel: {self.level}", True, (255, 255, 255))
        time_text = self.font.render(f"Tiempo: {int(self.time_left)}", True, (255, 255, 255))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        self.screen.blit(time_text, (self.width - 150, 10))

        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = ChromaticSpiderGame()
    game.run()