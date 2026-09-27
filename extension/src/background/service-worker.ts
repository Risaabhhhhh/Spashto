/// <reference types="chrome"/>

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "spashto-simplify",
    title: "Simplify this",
    contexts: ["selection"]
  });
  
  // Allow opening side panel on action click
  chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch(console.error);
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "spashto-simplify" && info.selectionText) {
    // Save the selected text to storage and open side panel
    chrome.storage.local.set({ spashto_selected_text: info.selectionText }, () => {
      if (tab?.windowId) {
        chrome.sidePanel.open({ windowId: tab.windowId });
      }
    });
  }
});
