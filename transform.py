def transform(self, x, y):
    if self.MODE_2D == 1:
        return x, y
    else:
        lin_y = y * self.perspective_point_y / self.height

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y

        factor_y = diff_y / self.perspective_point_y
        factor_y = pow(factor_y, 4)

        tr_x = self.perspective_point_x + diff_x * factor_y
        tr_y = self.perspective_point_y - factor_y * self.perspective_point_y

        return int(tr_x), int(tr_y)
