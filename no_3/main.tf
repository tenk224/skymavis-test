resource "aws_iam_group" "group" {
  for_each = var.github_team_member
  name = each.key
}

resource "aws_iam_user" "user" {
  for_each = var.github_user
  name = each.key
}

resource "aws_iam_group_membership" "membership" {
  for_each = var.github_team_member
  name = each.key
  group = each.key
  users = each.value
  depends_on = [
    aws_iam_user.user,
    aws_iam_group.group
  ]
}

resource "aws_iam_user_policy" "maintainer" {
  for_each = var.github_team_maintainer
  name = each.key
  user = each.value
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
  depends_on = [
    aws_iam_user.user
  ]
}