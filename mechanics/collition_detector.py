class CollitionDetector:
    def is_collided_with(self, rect1, rect2):
        return rect1.colliderect(rect2)
