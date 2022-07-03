// SPDX-License-Identifier: MIT
pragma experimental ABIEncoderV2;
pragma solidity ^0.6.6;

contract Todo {
    struct TodoModel {
        string name;
        bool completed;
    }

    struct UserListWithTodos {
        address user;
        TodoModel[] todos;
    }

    // this function helps to map the todos to the user
    mapping(address => UserListWithTodos) todos;

    // this function helps to add user to-dos to the mapping
    function addTodo(address user, string memory name) public {
        if (todos[user].todos.length == 0) {
            todos[user].user = user;
            todos[user].todos.push(TodoModel(name, false));
        } else {
            todos[user].todos.push(TodoModel(name, false));
        }
    }


    // get the todos of the user
    function getTodos(address user) public view returns (TodoModel[] memory) {
        return todos[user].todos;
    }

    // change the status of the todo
    function changeStatus(address user, uint index) public {
        todos[user].todos[index].completed = !todos[user].todos[index].completed;
    }

}
