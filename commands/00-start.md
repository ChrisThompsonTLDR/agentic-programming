# Initialize New Epic

## Behavior
If invoked without additional input, prompt the user:
> "What is the title of the new epic?"

If a title was supplied inline (e.g., `00-start "RPG Mounts System"`), skip the prompt.

---
## Preparation

1. **Read all files in `.cursor/support`**.

---

## Steps

1. **Collect Epic Title**
   - If no arguments provided → ask user for title.
   - If argument provided → use directly.
   - Convert title to slug form:  
     `slug = title.toLowerCase().replaceAll(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')`

2. **Create Epic Task**
   - Call `mcp_task_master_ai_add_task`  
     **Parameters:**
     - `title`: `"EPIC: " + title`
     - `tag`: `"epics"`
     - `status`: `"deferred"`
     - `description`: `New epic initialized via 00-start command.`
   - Capture returned `task_id` AKA `epic_id`.

3. **Generate Folder**
   - Path:  
     `.taskmaster/epics/${task_id.padStart(3,'0')}_${slug}/`
   - Create directory recursively if missing.

4. **Update the epic**
   - Call `mcp_task_master_ai_update_task`  
     **Parameters:**
     - `id`: epic_id
     - `tag`: `"epics"`
     - prompt: `"Add the epic path to the numbered artifacts list."`
5. **Reply**
   - `The epic path is <path to epic>`
   - exactly that and nothing else
