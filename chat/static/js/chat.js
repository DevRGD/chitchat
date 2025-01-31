const users = [
  {
    id: 1,
    name: 'Connie Bell',
    lastChat: 'Seen 5m ago',
    img: 'connie.jpg',
    chats: [
      { senderId: 2, senderName: 'Connie', senderImg: 'connie.jpg', message: 'Hey! Are we still meeting at 5?', time: '4:45 PM', status: 'seen', type: 'received' },
      { senderId: 1, senderName: 'me', senderImg: 'me.jpg', message: 'Yes! See you soon!', time: '4:46 PM', status: 'sent', type: 'sent' },
    ],
  },
  {
    id: 2,
    name: 'Peter Tapia',
    lastChat: 'Delivered 2m ago',
    img: 'peter.jpg',
    chats: [
      { senderId: 1, senderName: 'me', senderImg: 'me.jpg', message: 'Hey, did you send the photos?', time: '3:30 PM', status: 'delivered', type: 'sent' },
      { senderId: 2, senderName: 'Peter', senderImg: 'peter.jpg', message: 'Just sent them!', time: '3:31 PM', status: 'seen', type: 'received' },
    ],
  },
  { id: 3, name: 'Dianne Lambert', lastChat: 'Offline', img: 'dianne.jpg', chats: [] },
];

document.addEventListener('DOMContentLoaded', () => {
  const userList = document.getElementById('userList');
  const chatBox = document.getElementById('chatBox');
  const chatHeader = document.getElementById('chatHeader');

  users.forEach((user, index) => {
    const li = document.createElement('li');
    li.className = 'p-3 bg-gray-100 rounded-lg flex items-center cursor-pointer';
    li.innerHTML = `<img src="${user.img}" class="w-8 h-8 rounded-full mr-3"> <div><p class="font-bold">${user.name}</p><p class="text-sm text-gray-500">${user.lastChat}</p></div>`;
    li.onclick = () => loadChat(index);
    userList.appendChild(li);
  });

  function loadChat(index) {
    chatBox.innerHTML = '';
    chatHeader.innerText = users[index].name;
    users[index].chats.forEach((chat) => {
      const chatDiv = document.createElement('div');
      chatDiv.className = chat.type === 'sent' ? 'text-right' : 'text-left';
      chatDiv.innerHTML = `<div class="flex items-center ${chat.type === 'sent' ? 'justify-end' : ''}">
          <img src="${chat.senderImg}" class="w-6 h-6 rounded-full mr-2">
          <p class="${chat.type === 'sent' ? 'bg-blue-500' : 'bg-purple-400'} text-white p-2 rounded-lg inline-block">
            ${chat.message} <span class='text-xs text-gray-300'>${chat.time} - ${chat.status}</span>
          </p>
        </div>`;
      chatBox.appendChild(chatDiv);
    });
  }

  document.getElementById('sendButton').addEventListener('click', () => {
    const messageInput = document.getElementById('messageInput');
    if (messageInput.value.trim() === '') return;

    const activeUserIndex = users.findIndex((user) => user.name === chatHeader.innerText);
    if (activeUserIndex === -1) return;

    const newMessage = {
      senderId: 1,
      senderName: 'me',
      senderImg: 'me.jpg',
      message: messageInput.value,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      status: 'sent',
      type: 'sent',
    };

    users[activeUserIndex].chats.push(newMessage);
    loadChat(activeUserIndex);
    messageInput.value = '';
  });
});
