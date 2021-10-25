variable "github_user" {
  type = set(string)
  default = [
    "User1",
    "User2",
    "User3",
    "User4",
    "User5",
    "User6",
    "User7",
    "User8",
    "User9",
    "User10",
  ]
}

variable "github_team_maintainer" {
  type = map(string)
  default = {
    Team1 = "User2"
    Team2 = "User1"
    Team3 = "User3"
    Team4 = "User2"
    Team5 = "User1"
    Team6 = "User4"
  }
}

variable "github_team_member" {
  type = map(set(string))
  default = {
    Team1 = [
      "User1",
      "User2",
      "User3",
      "User5",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    Team2 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    Team3 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User5",
      "User6",
      "User7"
    ]
    Team4 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User5",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    Team5 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User6",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
    Team6 = [
      "User1",
      "User2",
      "User3",
      "User4",
      "User5",
      "User7",
      "User8",
      "User9",
      "User10",
    ]
  }
}