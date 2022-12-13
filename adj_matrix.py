def get_visibility_ally_matrix(self):
    """Returns a int numpy array of dimensions
    (n_agents, n_agents) indicating which units
    are visible to each agent.
    """
    arr = np.zeros(
        (self.n_agents, self.n_agents),
        dtype=np.long,
    )

    for agent_id in range(self.n_agents):
        current_agent = self.get_unit_by_id(agent_id)
        arr[agent_id,agent_id] = 1
        if current_agent.health > 0:  # it agent not dead
            x = current_agent.pos.x
            y = current_agent.pos.y
            sight_range = self.unit_sight_range(agent_id)
            al_ids = [
                al_id for al_id in range(self.n_agents)
                if al_id > agent_id
            ]
            for i, al_id in enumerate(al_ids):
                al_unit = self.get_unit_by_id(al_id)
                al_x = al_unit.pos.x
                al_y = al_unit.pos.y
                dist = self.distance(x, y, al_x, al_y)

                if (dist < sight_range and al_unit.health > 0):
                    # visible and alive
                    arr[agent_id, al_id] = arr[al_id, agent_id] = 1
    return arr