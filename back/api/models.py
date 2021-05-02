from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

# メンバー
class Member(models.Model):
    class Meta:
        verbose_name = 'メンバー'
        verbose_name_plural = 'メンバー'
        db_table = "Member"

    # メンバーID
    member_id = models.AutoField(primary_key=True, editable=False)
    # last name
    last_name = models.CharField('氏', max_length=20)
    # first name
    first_name = models.CharField('名', max_length=20)
    # ニックネーム
    nick_name = models.CharField('ニックネーム', max_length=20)
    # number
    number = models.IntegerField('背番号', null=False)
    
    def __str__(self):
        return self.last_name + self.first_name

# ポジション
class Position(models.Model):
    class Meta:
        verbose_name = 'ポジション'
        verbose_name_plural = 'ポジション'
        db_table = "Position"

    # ポジションID
    position_id = models.IntegerField(primary_key=True)
    position_name = models.CharField(max_length=20)

    def __str__(self):
        return self.position_name


# メンバーポジション
class MemberPosition(models.Model):
    class Meta:
        verbose_name = '守備位置'
        verbose_name_plural = '守備位置'
        db_table = "MemberPosition"

    # ポジションID
    member_position_id = models.AutoField(primary_key=True, editable=False)
    # メンバー
    member = models.ForeignKey(Member, related_name='member_position_member', on_delete=CASCADE, null=False)
    # ポジション
    position = models.ForeignKey(Position, related_name='member_position_position', on_delete=CASCADE, null=False)
    # ポジションレベル(メイン、サブ)
    position_level = models.IntegerField('ポジションレベル', null=False)

    def __str__(self):
        return self.member.last_name + self.member.first_name